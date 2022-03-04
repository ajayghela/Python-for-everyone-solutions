"""
Exercise  11.1: Write a simple program to simulate the operation of the grep
command on Unix. Ask the user to enter a regular expression and count the
number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$

"""

import re
fname = input("Enter a File: ")
fhand = open(fname)
input_ex = input("Enter a Regular Expression:")
reg_ex = str(input_ex)
count = 0


for lines in fhand:
    line = lines.rstrip()
    if re.findall(reg_ex, line):
        count = count + 1

print(fname + " had " + str(count) + " lines that matched " + reg_ex)
