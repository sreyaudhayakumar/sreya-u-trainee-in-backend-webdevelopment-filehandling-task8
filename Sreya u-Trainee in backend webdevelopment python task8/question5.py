# 5)Write a Python program to copy the contents of a file to another file. 

input_file = "input_file.txt"
output_file = "output_file.txt"

input = open(input_file, "r")
output = open(output_file, "w")

output.write(input.read())

input.close()
output.close()

print("Contents of", input_file, "have been copied to", output_file)
