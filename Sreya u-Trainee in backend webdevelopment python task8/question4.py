# 4)Write a Python program to read a file line by line store it into a variable.

file_name = "filetask1.txt"
lines = []

file = open(file_name, "r")
for line in file:
    lines.append(line.strip())

file.close()  

print(lines)
