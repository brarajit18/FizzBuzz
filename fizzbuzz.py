# -*- coding: utf-8 -*-
import numpy as np

class FizzBuzz():
    """This code solves the FizzBuzz problems,
    which is used to detect the number divisible 
    with 3 (Fizz), divisible by 5 (Buzz), and 
    both (FizzBuzz).
    All numbers, which are not divisible by either 3
    or 5 are displayed as is.
    Syntax Example:
        fizz = FizzBuzz()
        x = 20; #to check first 20 numbers (Fizz, Buzz, FizzBuzz 
        # or not divisble with 3 and/or 5)
        print (fizz.FizzBuzz(x))
    Note: Please note, that function & class have same name.
    So don't get confused with class object, and function call.
    """
    def FizzBuzz(self, numCount):
        result = [];
        for i in range(1,numCount):
            if i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif (i % 5 == 0)  and (i % 3 == 0):
                result.append('FizzBuzz')
            else:
                result.append(i)
        return result

if __name__ == '__main__':
    fizz = FizzBuzz()
    x = 20; #to check first 20 numbers (Fizz, Buzz, FizzBuzz 
    # or not divisble with 3 and/or 5)
    print (fizz.FizzBuzz(x))
    
""" 
This code snippet is used to find the numbers
between certain range in given array
"""
#for x in fibo:
#    if x < 10 or x > 20:
#        print (x)
""" 
This snippet applies square to whole array
using numpy array
"""
#print (np.asarray(fibo) ** 2)