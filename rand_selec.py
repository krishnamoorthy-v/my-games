#!/usr/bin/python3

import random as ra
import os
import csv
import time

cache = [] # used to store frequently using data to avoid repeated selection of student again and again

def create_stud_list():
    list_file_dir = os.listdir()
    if "stud_list_dir.csv" not in list_file_dir:
        strength = int(input("Enter the strength of the student: "))
        with open("stud_list_dir.csv", 'w') as f:
            writer = csv.writer(f)
            for i in range(1, strength+1):
                writer.writerow([i, str(input("Enter the name {} ".format(i)))])

def csv_to_dict():
    stud_dict = {}
    list_file_dir = os.listdir()
    if "stud_list_dir.csv" in list_file_dir:
        with open("stud_list_dir.csv", 'r') as f:
            reader = csv.reader(f)
            for i in reader:
                stud_dict[i[0]] = i[1]
    return stud_dict  

#create_stud_list()



def rand_engine(data):
    while(True):
        choice = str(ra.randint(1, len(data)))
        if data[choice] not in cache:
            cache.append(data[choice])
            break
        else:
            continue
    return data[choice]

def rand_select(data, n):
    ex_stud = len(data) - len(cache)

    if n <= ex_stud:
        for i in range(n):
            #time.sleep(3)
            print("\t  ",rand_engine(data))
    elif ex_stud < n:
        for i in range(ex_stud):
            print("\t  ", rand_engine(data))
        print('\n*********cache is full***********')
    elif n > ex_stud:
        print("\n**********cache is full**********")
#rand_select(3)
print("\t\tchoice \n 1 create a data. \n 2 select the student . \n 3 clear cache. \n 4 exit. \n")
while(True):
    choose = str(input("\nEnter your choice: "))
    if choose == '1':
        create_stud_list()
        data = csv_to_dict()

    elif choose == '2':
        
        n = int(input("\n\tEnter the number of selection: "))
        rand_select(data, n)

    elif choose == "3":
        cache.clear()

    elif choose == "4":
        exit()

    else:
        print("Wrong choice try again")