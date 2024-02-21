# 10)	Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.

def alphabet(file_name, letters):
    file = open(file_name, 'w')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

   
    for i in range(0, len(alphabet), letters):
        line = alphabet[i:i+letters]
        file.write(line + '\n')
        
    file.close()

file_name = input("Enter the name of the file to create: ")


letters = int(input("Enter the number of letters per line: "))
alphabet(file_name, letters)


print(f"File '{file_name}' created successfully with {letters} letters per line.")
