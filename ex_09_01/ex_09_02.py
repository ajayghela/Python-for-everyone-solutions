"""
Exercise  9.2: Write a program that categorizes each mail message by which day
of the week the commit was done. To do this, look for lines that start with
"From", then look for the third word and keep a running count of each of the
days of the week. At the end of the program, print out the contents of your
dictionary (order does not matter).
Sample Line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dictionary_days = dict()
for line in fhand:
    if line.startswith('From '):        #only looks at lines beginning with 'From '
        day = line.split()[2]           # splits the line and assigns the varaible day the string that is indexed to the integer 2.
        dictionary_days[day] = dictionary_days.get(day, 0) + 1 # looks for the key day, assigning the value 0 if not present, otherwise adding 1

print(dictionary_days)
