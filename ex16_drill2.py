from sys import argv

path, filename = argv

file = open(filename)
print(file.read())

file.close()