filePath = input("Please enter the path of the file\n")

file = open(filePath, "rt")
contents = file.read()
file.close()
dictionary = contents.replace("\n", "")
file = open(filePath, "wt")
file.write(dictionary)
