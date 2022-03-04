"""
Exercise  9.3: Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email
address, and print the dictionary.
Enter file name: mbox-short.txt
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dictionary_mail = dict()
for line in fhand:
    if line.startswith('From '):
        mail = line.split()[1]
        dictionary_mail[mail] = dictionary_mail.get(mail,0) + 1
        #if mail in dictionary_mail:
            #dictionary_mail[mail] = dictionary_mail[mail] + 1
        #else :
            #dictionary_mail[mail] = 1


print(dictionary_mail)
