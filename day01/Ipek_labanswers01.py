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
    if num >= 500:
        integer.append("D")
        integer.append("C" * ((num-500)//100))
    return(integer)
    
    if num == 1:
        return("I")
    elif num == 2:
        return("II")
    elif num == 3:
        return("III")
    elif num == 4:
        return("IV")
    elif num == 5:
        return("V")    
    elif num == 6:
        return("VI")
    elif num == 7:
        return("VII")
    
    else:
        return("TBD")

  
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