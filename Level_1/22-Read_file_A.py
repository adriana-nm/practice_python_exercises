# 22.A) Read from file

# Given a .txt with names, count how many names are in the file

# Creates a dictionary of the words in the file
d = {}
with open('read_fileA.txt', 'r') as open_file:
    line = open_file.readline().rstrip('\n')
    while line:
        if line not in d.keys():
             d[line] = 1
        else:
             d[line] += 1
        line = open_file.readline().rstrip('\n')
print(d)


# Creates a dictionary of the letters in the file
d = {}
with open('read_fileA.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        for letter in line:
            if word not in d.keys():
                d[word] = 1
            else:
                d[word] += 1
        line = open_file.readline()
print(d)