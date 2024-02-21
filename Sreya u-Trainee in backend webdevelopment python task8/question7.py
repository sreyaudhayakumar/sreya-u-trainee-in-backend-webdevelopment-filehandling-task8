# 7)	Write a Python program to assess if a file is closed or not.

def file_closed(file_name):
    try:
        file = open(file_name, 'r')
        is_closed = file.closed
        file.close()
        if is_closed:
            print(f"{file_name} is closed.")
        else:
            print(f"{file_name} is open.")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

file_name = input("Enter the file name: ")
file_closed(file_name)

