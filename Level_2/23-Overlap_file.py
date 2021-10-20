# 23) File Overlap

# There are two .txt files that have list of number
# First .txt has all prime numbers under 1000
# Second .txt has all happy numbers up to 1000
# Find numbers that are overlapping

def create_list(namelist):
    lnums =  []
    with open(namelist, 'r') as open_file:
        line = open_file.readline().strip('\n')
        while line:
            lnums.append(line)
            line = open_file.readline().strip('\n')
    return lnums


def overlap_num():
    list3 = []
    list1 = create_list('overlap_file_1.txt')
    list2 = create_list('overlap_file_2.txt')
    for num in list1:
        if num in list2:
            list3.append(num)
    print(list3)

overlap_num()