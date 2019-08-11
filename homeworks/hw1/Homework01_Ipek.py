from datetime import datetime
import scipy as sp
sp.random.seed(123345)
class Portfolio():
	def __init__(self):
		self.CashAmount = 0
		self.StockShare = dict()
		self.MF = dict()
		self.hist = []
		self.balance = []
		self.time = []
	#Prints the Portfolio
	def __str__(self):
		ss = []
		mf = []
		for i in list(self.StockShare.keys()):
			x = "%s %s"%(self.StockShare[i][0], i)
			ss.append(x)
		for i in list(self.MF.keys()):
			y = "%.2f %s"%(self.MF[i], i)
			mf.append(y)
		return "cash: %.2f \nstock: %s \nmutual funds: %s" %(self.CashAmount, ss, mf)
	def addCash(self, amount):
		self.CashAmount += amount
		self.hist.append("+ $%.2f" %amount)
		self.balance.append("$%.2f" %self.CashAmount)
		now = datetime.now()
		self.time.append(now.strftime("%d-%b-%Y %H:%M:%S"))
	def withdrawCash(self,amount):
		if amount <= self.CashAmount:
			self.CashAmount -= amount
			self.hist.append("- $%.2f" %amount)
			self.balance.append("$%.2f" %self.CashAmount)
			now = datetime.now()
			self.time.append(now.strftime("%d-%b-%Y %H:%M:%S"))
		else:
			print("Non-sufficient Funds")
	def buyStock(self, share, stock):
		newstockportfolio = {stock.symbol: [share, stock.price]}
		if stock.price * share <= self.CashAmount:
			if stock.symbol in list(self.StockShare.keys()):
				newstockportfolio[stock.symbol][0] == share + self.StockShare[stock.symbol][0]
				self.StockShare.update([(stock.symbol, [(self.StockShare[stock.symbol][0] + share),self.StockShare[stock.symbol][1]])])
			else:
				self.StockShare.update(newstockportfolio)
			self.CashAmount -= stock.price * share
			self.hist.append("+ %s %s" % (share, stock.symbol))
			self.balance.append("$%.2f" %self.CashAmount)
			now = datetime.now()
			self.time.append(now.strftime("%d-%b-%Y %H:%M:%S"))
		else:
			print("Non-sufficient Funds")
	def sellStock(self, symbol, share):
		x=sp.random.uniform(low=(self.StockShare[symbol][1] * (1/2)) ,high=(self.StockShare[symbol][1] * (3/2)),size=1)
		if symbol in list(self.StockShare.keys()):
			if share <= self.StockShare[symbol][0]:
				self.StockShare.update([(symbol, [(self.StockShare[symbol][0] - share),self.StockShare[symbol][1]])])
				self.CashAmount += x[0] * share
				self.hist.append("- %s %s" % (share, symbol))
				self.balance.append("$%.2f" %self.CashAmount)
				now = datetime.now()
				self.time.append(now.strftime("%d-%b-%Y %H:%M:%S"))
			else:
				print("Non-sufficient Shares")
		else:
			print("Non-Existing Stock")
	def buyMutualFund(self, share, funds):
		newMF = {funds.symbol: share}
		if share <= self.CashAmount:
			if funds.symbol in list(self.MF.keys()):
				newMF[funds.symbol] == share + self.MF[funds.symbol]
				self.MF.update([(funds.symbol, (self.MF[funds.symbol] + share))])
			else:
				self.MF.update(newMF)
			self.CashAmount -= share
			self.hist.append("+ %.2f %s" % (share, funds.symbol))
			self.balance.append("$%.2f" %self.CashAmount)
			now = datetime.now()
			self.time.append(now.strftime("%d-%b-%Y %H:%M:%S"))
		else:
			print("Non-sufficient Funds")
	def sellMutualFund(self, symbol, share):
		x=sp.random.uniform(0.9,1.2,1)
		if symbol in list(self.MF.keys()):
			if share <= self.MF[symbol]:
				self.MF.update([(symbol, (self.MF[symbol] - share))])
				self.CashAmount -= x[0] * share
				self.hist.append("- %s %s" % (share, symbol))
				self.balance.append("$%.2f" %self.CashAmount)
				now = datetime.now()
				self.time.append(now.strftime("%d-%b-%Y %H:%M:%S"))
			else:
				print("Non-sufficient Shares")
		else:
			print("Non-Existing Mutual Funds")
	def history(self):
		data = list(map(list, zip(*[self.hist,self.balance,self.time])))
		dash = '-' * 55
		print(dash)
		print('{:<15s}{:^14s}{:^26s}'.format("Transaction", "Balance", "Date"))
		print(dash)
		for i in range(len(data)):
			print('{:<10s}{:>15s}{:>30s}'.format(data[i][0],data[i][1],data[i][2]))



class Stock:
	def __init__(self, price, symbol):
		self.price = price
		self.symbol = symbol


class MutualFund:
	def __init__(self, symbol):
		self.symbol = symbol

