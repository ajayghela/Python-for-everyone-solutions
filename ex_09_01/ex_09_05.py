"""
Exercise  9.5: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of
your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
['media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1,
'caret.cam.ac.uk': 1, 'iupui.edu': 8}

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
        d_pos = mail.find("@")
        #print(d_pos)  slices the string to get the character before the domain name
        domain = mail[d_pos + 1:] #domain = mail.split('@')[1]
        #print(domain) the domain variable now conatains the everything after the @ within the index [1]
        dictionary_mail[domain] = dictionary_mail.get(domain,0) + 1

print(dictionary_mail)

largest_value = 0
for k,v in dictionary_mail.items():
    #print(k,v)
    if v > largest_value :
        largest_value = v
        largest_key = k

#max_key = max(dictionary_mail, key = dictionary_mail.get)

print(largest_key, largest_value)
