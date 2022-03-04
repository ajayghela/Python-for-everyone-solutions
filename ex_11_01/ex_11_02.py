"""
Exercise  11.2: Write a program to look for lines of the form
'New Revision: 39771'
and extract the number from each of the lines using a regular expression and
the findall() method. Compute the average of the numbers and print out the
average.

Enter file:mbox.txt
38549.7949721
Enter file:mbox-short.txt
39756.9259259

"""

import re
fname = input("Enter a File: ")
fhand = open(fname)
lst = []


for lines in fhand:
    line = lines.rstrip()
    num = re.findall('^New\sRevision:\s.([0-9.]+)', line)
    if len(num) > 0:
        for number in num:
            number = int(number)
            lst.append(number)        
    
        
lst_count= len(lst)
total = sum(lst)
print(total/lst_count)
        



        
