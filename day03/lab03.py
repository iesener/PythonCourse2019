import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
	if type(txt) != str:
		raise TypeError("Enter an integer!")
	else:
		return txt.upper()

## reverse all characters in string
def reverse(txt):
	x = list(txt)
	x.reverse()
	if type(txt) != str:
		raise TypeError("Enter an integer!")
	else:
		return ''.join(x)

## reverse word order in string
def reversewords(txt):
	x = txt.split()[::-1]
	if type(txt) != str:
		raise TypeError("Enter an integer!")
	else:
		return ' '.join(x)


## reverses letters in each word
def reversewordletters(txt):
	x = txt.split()
	y =[]
	if type(txt) != str:
		raise TypeError("Enter an integer")
	else:
		for i in x:
			i.reverse()
			return ' '.join(i)

		
## change text to piglatin.. google it! 
def piglatin(txt):




## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


		
			
			
			
			
			
			

