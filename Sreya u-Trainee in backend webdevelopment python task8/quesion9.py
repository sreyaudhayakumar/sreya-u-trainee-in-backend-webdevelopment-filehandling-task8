# 9)Write a Python program that takes a text file as input and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.

def count_words(file_name):
    try:
        file = open(file_name, 'r')
        content = file.read().replace(',', ' ')
        num_words = len(content.split())
        file.close()
        return num_words
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return -1

file_name = input("Enter the name of the text file: ")
words = count_words(file_name)
if words != -1:
    print(f"The number of words in the file '{file_name}' is: {words}")
 