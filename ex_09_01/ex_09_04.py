"""
Exercise  9.4: Add ccode to the above program to figure out who has the most
mesasges in the file.
After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section [maximumloop]) to
find who has the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.ed 5
Enter a file name: mbox.txt
zqian@umich.edu 195

"""
fname = input("Enter a File Name: mbox-short.txt")
try:
    if len(fname) < 1 : fname = 'mbox-short.txt'

except:
    print('File cannot be opened:', fname)
    exit()

fhand = open(fname)

dictionary_mail = dict()
for line in fhand:
    if line.startswith('From '):
        #print(line)
        mail = line.split()[1]
        #print(mail)
        dictionary_mail[mail] = dictionary_mail.get(mail,0) + 1

#print(dictionary_mail)

largest_value = 0
for k,v in dictionary_mail.items():     #items returns a list of dict's (key, value).
    #print(k,v)
    if v > largest_value :
        largest_value = v           #goes through the dictionary replacing the largest_value with with v once a larger value is found.
        largest_key = k             #sets the largest_key, k, to correspond with v.

#max_key = max(dictionary_mail, key = dictionary_mail.get)

print(largest_key, largest_value)
