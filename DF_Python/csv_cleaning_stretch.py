# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:06:21 2021

@author: owatson2
"""

# import os
# print(os.getcwd())
# os.chdir("DF_Python")


def clean_csv(filename):
    
    #Opening and creating the necessary files
    excel = open(filename, "r")
    excel_cleaned = open("csv_cleaned.csv", "w")
    excel_old = open("csv_old.csv", "w")
    
    count_ls = []
    
    #Iterating through to select the rows with the correct number of columns
    for i in excel:
        count = 0
        for j in i:
            if j == ',':
                count += 1
        count_ls.append(count)
        if count == count_ls[0]:
            excel_cleaned.write(i)
        else:
            excel_old.write(i)
    excel.close()
    excel_cleaned.close()
    excel_old.close()
    
    #Reopening the correct files and printing them
    excel_cleaned = open("csv_cleaned.csv", "r")
    excel_old = open("csv_old.csv", "r")
    
    print(excel_cleaned.read())
    print(excel_old.read())
    
#clean_csv("csv_cleaning.csv")

excel_old_cleaned = open("csv_old_cleaned", "w")
for i in range(0,2):
    if i == 0:
        excel_old_cleaned.write("Alice, 27, 1 Main Street - Townsville - Berks, My friend recommended it, 8")
    else:
        excel_old_cleaned.write("Carla, 17, My House, I’ve always been interested and now seemed like a great time, 5")
excel_old_cleaned.close()

excel_old_cleaned = open("csv_old_cleaned", "r")
print(excel_old_cleaned.read())