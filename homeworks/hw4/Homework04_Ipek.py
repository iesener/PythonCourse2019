### Ipek Ece Sener
### Homework 04

import random
import time
from decimal import Decimal

def pancake(mylist):
	for i in range(len(mylist),1, -1):
		second = mylist[(mylist.index(max(mylist[:i]))+1):i]
		third = mylist[i:]
		mylist = mylist[:(mylist.index(max(mylist[:i]))+1)]
		mylist.reverse()
		mylist.extend(second)
		mylist.reverse()
		mylist.extend(third)
	return mylist


def merge_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    mid = len(mylist) // 2 
    left = merge_sort(mylist[:mid]) 	# Divide both halves until they have one element each.
    right = merge_sort(mylist[mid:]) 
    return merge(left, right, mylist.copy())


def merge(left, right, merged):   # This function is to merge each element that was divided above.
    L = 0
    R = 0
    while L < len(left) and R < len(right): 
        if left[L] <= right[R]:
            merged[L + R]=left[L]
            L += 1
        else:
            merged[L + R] = right[R]
            R += 1
    for L in range(L, len(left)):
        merged[L + R] = left[L] 
    for R in range(R, len(right)):
        merged[L + R] = right[R] 
    return merged


    
pancake_time = []
merge_time = [] 

for i in range(1,1001):
	l = random.sample(range(1,1001), i) 
	a = Decimal(time.time())
	pancake(l)
	b = Decimal(time.time())
	pancake_time.append(b-a)
	a = Decimal(time.time())
	merge_sort(l)
	b = Decimal(time.time())
	merge_time.append(b-a)


import matplotlib.pyplot as plt

x = range(1, 1001) ## # of elements in list 
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
pan, = plt.plot(x,pancake_time, color = 'orchid')
mer, = plt.plot(x,merge_time, color = 'yellowgreen')
plt.legend([pan, mer], ['Pancake Sorting', 'Merge Sorting'], loc = "upper left", prop = {"size":10})
plt.ylabel("Time")
plt.xlabel("Number of Elements in the List")
plt.title("The Effect of Different Sort Algorithms on Runtime")
plt.savefig('plot2.pdf')




    