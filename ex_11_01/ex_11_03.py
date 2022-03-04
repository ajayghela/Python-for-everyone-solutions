import re
fname = input("Enter a File: ")
try:
    if len(fname) <1 : fname = "regex_sum_1291504.txt"
except:
    exit()
fhand = open(fname)
lst = []


for lines in fhand:
    line = lines.rstrip()
    num = re.findall('([0-9]+)', line)
    if len(num) > 0:
        for number in num:
            number = int(number)
            lst.append(number)        
        

total = sum(lst)
print(total)
        



        
