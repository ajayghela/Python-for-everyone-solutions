"""
Exercise  8.4: Download a copy of the file from www.py4e.com/code3/romeo.txt
Write a program to open the file romeo.txt and read it line by line. For each
line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is
not in the list, add it to the list.
When the program completes, sort and print the resulting words in alphabetical
order.
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east',
'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick',
'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

"""
mylist = []
fhand = open('romeo.txt')
for line in fhand:
    line = line.rstrip()
    #print('line:', line)
    words = line.split()     #I've got each line ready
    #print('word:', word)
    for word in words:
        if word in mylist:      #skips any repeated words
            continue
        mylist.append(word)     #adds the word to the list
        #print(mylist)         #debugging check

final_list = sorted(mylist)     #sorted alphabetically

print('Enter file: romeo.txt')
print(final_list)

