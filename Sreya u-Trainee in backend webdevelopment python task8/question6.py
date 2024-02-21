# 6)Write a Python program to read a random line from a file.

import random

def read_random_line(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    return random.choice(lines).strip()

file_name = "filetask1.txt"  
random_line = read_random_line(file_name)
print("Random line from", file_name, ":", random_line)
