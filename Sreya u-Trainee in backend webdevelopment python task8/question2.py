# 2)	Write a Python program to read first n lines of a file.

file_name = "filetask1.txt"
n_lines = int(input("Enter the number of lines to read: "))

with open(file_name, "r") as file:
    lines = file.readlines()[:n_lines]  
    for line in lines:
        print(line.strip())  

