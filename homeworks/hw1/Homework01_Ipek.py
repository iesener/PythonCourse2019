class Portfolio():
	def __init__(self):
		self.CashAmount = 0
		self.StockShare = dict()
		self.MF = dict()
	#Prints the Portfolio
	def __str__(self):
		return "cash: %s \nstock: %s \nMutual Funds: %s" %(self.CashAmount, self.StockShare, self.MF)
	def addCash(self, amount):
		self.CashAmount += amount
	def withdrawCash(self,amount):
		if amount <= self.CashAmount:
			self.CashAmount -= amount
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
		else:
			print("Non-sufficient Funds")
	def sellStock(self, symbol, share):
		import scipy as sp
		sp.random.seed(123345)
		x=sp.random.uniform(low=(self.StockShare[symbol][1] * (1/2)) ,high=(self.StockShare[symbol][1] * (3/2)),size=1)
		uni = round(x[0],2)
		if symbol in list(self.StockShare.keys()):
			if share <= self.StockShare[symbol][0]:
				self.StockShare.update([(symbol, [(self.StockShare[symbol][0] - share),self.StockShare[symbol][1]])])
				self.CashAmount += uni * share
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
		else:
			print("Non-sufficient Funds")
	def sellMutualFund():
		import scipy as sp
		sp.random.seed(123345)
		x=sp.random.uniform(0.9,1.2,1)
		uni = round(x[0],2)		





class Stock:
	def __init__(self, price, symbol):
		self.price = price
		self.symbol = symbol


class MutualFund:
	def __init__(self, symbol):
		self.symbol = symbol


port = Portfolio()
port.addCash(500)
port.buyStock(5,deneme)
port.buyStock(8,deneme2)
print(port)
port.buyStock(2,deneme2)
print(port)
port.sellStock("HTM",2)
print(port)
port.sellStock("BLB",3)
print(port)

deneme = Stock(5, "HTM")
deneme2 = Stock(10, "BLB")
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
port.buyMutualFund(10.3, mf1) 
port.buyMutualFund(2, mf2)
print(port)


