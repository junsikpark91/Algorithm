# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:49:24 2021

@author: pok99
"""

#Exchanging Coin - Greedy Algorithm
# Counting the number of coins (Minimum)

"""The greedy approach does not always guarantees optimal solution 
   The best solutions are guaranteed when the exchanges are the multiples of each other
   To solve with randomly given coins, dynamic programming should be used """

N = int(input()) # Received Money

Change = [100,20,10,5,1]
count =0 

for coin in Change:
    count += N//coin
    print(f'The number of ${coin}: {N//coin}')
    N %= coin
    
print("The number of coins exchanged:",count)

    