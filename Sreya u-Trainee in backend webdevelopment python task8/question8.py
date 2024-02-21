# 8)	Write a Python program to write a list to a file.

def list(file_name, user_list):
    file = open(file_name, 'w')
    for item in user_list:
        file.write(str(item) + '\n')
    file.close()

user_list = input("Enter items for the list (separated by spaces): ").split()

file_name = "filetask1.txt"
list(file_name, user_list)
