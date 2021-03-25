# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:30:31 2021

@author: pok99
"""

from random import randint
import time
# Large number
# N: Total number of data
# M: The number of addition
# K: Limited number of adding the largest number in sequence


# Create 3 variables without space

N, M, K = map(int, input().split())

# Create a random N numbers 
data=[]

for _ in range(N):
    data.append(randint(1,10000))
data.sort() # Sorting input data
first = data[N-1] #Largest number
second = data[N-2] # Second Largest number

result =0

start_time = time.time()
while True:
    for i in range(K):
        if M==0:
            break
        result += first
        M -=1
    if M == 0:
        break
    result += second
    M-= 1

end_time = time.time()

print(result)
print(end_time-start_time)

#############################