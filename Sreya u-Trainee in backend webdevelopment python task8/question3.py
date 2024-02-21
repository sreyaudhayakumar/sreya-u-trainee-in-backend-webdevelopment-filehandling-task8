# 3)	Write a Python program to append text to a file and display the text

file = open('filetask1.txt', 'a')
file.write("grapes: Small, round, and succulent berries, available in various colors, prized for their sweet taste ")
file.close()

file = open('filetask1.txt', 'r') 
content = file.read()
print(content)
file.close()  
