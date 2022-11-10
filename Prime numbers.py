# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 02:20:05 2022

@author: Jon

A prime number is a number whose only divisors are 1 and itself.
  For example 1, 2, 3 5, 7, 11, 13 .. are prime numbers,
  but 9 (divisor of 3),  51 (divisor of 3) .. are not prime.

Write a python program to print out all the prime numbers < 1000
"""

from numpy import log, sqrt,ceil
from time import time
primes = []
topNumber = 1000
timeStart = time()
for i in range(2,topNumber):
    primeBool=True
    
    for j in range(2, i):
        #print (i,j,i1%)
        
        if i % j == 0:
            #print(f"{i} is not prime”)
            primeBool=False
            
    if primeBool: primes.append(i)
    
endTime = time()
executeTime = (endTime-timeStart)
print(f"execute time: {executeTime}")

print(f'primes: {primes}')

numberOfPrimes = len(primes)
estimateOfnumber = topNumber/log(topNumber)

print(f'number of primes less than {topNumber} is {numberOfPrimes}')
#print(f'log( {topNumber} ) is {log(topNumber)}')

print(f'estimated number of primes is {estimateOfnumber}')
percentErr = (numberOfPrimes-estimateOfnumber) /numberOfPrimes
print(f'percentErr: {percentErr*100}')