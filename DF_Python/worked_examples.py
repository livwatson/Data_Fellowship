# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:03:40 2021

@author: owatson2
"""

user_number = input("Enter a number: ")

try:
    number = float(user_number)
    if number < 7:
        print("Small")
    elif number >= 7 and number < 20:
        print("Medium")
    elif number >= 20:
        print("Large")
except:
    print("Error! Number not entered... Please try again")
    
    
    
animal = ['dog','cat','fish','elephant']

vowels = ['a', 'e', 'i', 'o', 'u']

def animals(letters, animals):
    output = []
    for i in range(len(animals)):
        split = list(animals[i])
        count = 0
        for j in range(len(vowels)):
            for k in range(len(split)):
                if vowels[j] == split[k]:
                    count += 1
        output.append([animals[i], count])
    return output

print(animals(vowels, animal))