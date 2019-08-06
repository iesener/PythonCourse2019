## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""

def binarify(num):
    remainder = []
    while num != 0:
        remainder.append(str(num % 2))
        num //= 2
    remainder.reverse()
    return ''.join(remainder)
    
"""convert positive integer to a string in any base"""
def int_to_base(num, base):
    remainder = []
    while num != 0:
        remainder.append(str(num % base))
        num //= base
    remainder.reverse()
    return ''.join(remainder)
    
"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
    integer = 0
    for i in range (1,len(string)+1):
        integer += base ** (i-1) * int(string[-i])
        print(integer)
    return(integer)
    

"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
    integer = 0
    for i in range (1,len(str1)+1):
        integer += base1 ** (i-1) * int(str1[-i])
    for i in range (1,len(str2)+1):
        integer += base2 ** (i-1) * int(str2[-i])
    return(integer)


"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
    integer = 0
    integer2 = 0
    for i in range (1,len(str1)+1):
        integer += base1 ** (i-1) * int(str1[-i])
    for i in range (1,len(str2)+1):
        integer2 += base2 ** (i-1) * int(str2[-i])
    return(integer * integer2)


"""given an integer, return the Roman numeral version"""
def romanify(num):
    integer = []
    integer.append("M" * (num // 1000))
    num %= 1000
    if  num >= 900:
        integer.append("CM")
    if  900 > num >= 500 :
        integer.append("D" + "C" * ((num-500)//100))
    if  500 > num >= 400 :
        integer.append("CD")
    if  400 > num :
        integer.append("C" * (num // 100))
    num %= 100
    if  num >= 90:
        integer.append("XC")
    if  90 > num >= 50 :
        integer.append("L" + "X" * ((num-50)//10))
    if  50 > num >= 40 :
        integer.append("XL")
    if  40 > num :
        integer.append("X" * (num // 10))
    num %= 10
    if  num == 9:
        integer.append("IX")
    if  9 > num >= 5 :
        integer.append("V" + "I" * (num-5))
    if  5 > num >= 4 :
        integer.append("IV")
    if  4 > num :
        integer.append("I" * num)
    return(integer)

romanify(3847)

  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.