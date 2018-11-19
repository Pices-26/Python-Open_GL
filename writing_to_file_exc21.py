import string

file = open('txt.txt', 'r')
file1 = open('txt1.txt', 'w')

file1.write(file.read().strip())

file.close()
file1.close()
