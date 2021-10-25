# 22.B) Read from file

# Given a .txt with long categories names count how many of each category are
# Need to parse the string

# With regex
import re

d = {}
with open('read_fileB.txt','r') as open_file:
    line = open_file.readline().rstrip('\n')
    while line:
        # Option 1: regex using sub
        # line = re.sub("/\w/","",line)
        # line = re.sub("/\w+\.jpg","", line)
        # line = re.sub("/\w+","", line)
        #Option 2 = regex using search + group
        search = re.search("/\w+/(\w+)", line)
        word = search.group(1)
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1
        line = open_file.readline().rstrip('\n')
print(d)


# # With string position
d = {}
with open('read_fileB.txt','r') as open_file:
    line = open_file.readline()
    while line:
        positstart = 3
        positend = line.find("/",3)
        word = line[3:positend]
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1
        line = open_file.readline()
print(d)