# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:24:54 2021

@author: RSKALA
"""

def creat_file():
    file = open("C:\\Users\\RSKALA\\OneDrive\\Desktop\\PYTON\\Lab-9\\First_Python_File.txt","w")
    file.write("First data \n")
    file.close()

    
    
def read_file():
    file = open("C:\\Users\\RSKALA\\OneDrive\\Desktop\\PYTON\\Lab-9\\First_Python_File.txt","r")
    line = file.readline()
    while line != '':
       print(line)
       line = file.readline()
    file.close()

def read_file2():
    file = open("C:\\Users\\RSKALA\\OneDrive\\Desktop\\PYTON\\Lab-9\\fruits.txt","r")
    file2 = open("C:\\Users\\RSKALA\\OneDrive\\Desktop\\PYTON\\Lab-9\\temp.txt","w")
    line = file.readline()
    while line != '':
        if line != 'Robin\n':
            file2.write(line)
        line = file.readline()
    
    file.close()
    file2.close()
    

def try_exception():
    
   numbers = ['nine', 'ten', 'eleven']
   sum = 0
   try:
       for s in numbers:
           n = int(s)
           sum += n
   except ValueError as err:
       print("Here is sum %d" %sum)
       return(err) 
    
try_exception()


