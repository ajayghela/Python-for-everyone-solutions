"""
Exercise  9.1: Write a program that reads the words in words.txt and stores
them as keys in a dictionary. Download a copy of the file from
https://www.py4e.com/code3/words.txt. It doesn't matter what the values are.
Then use the 'in' operator as a fast way to check whether a string is in the
dictionary.

"""
name = input('enter file:')
fhand = open(name)


dictionary_words = dict()  #creates the dictionary
for line in fhand:
    words = line.split()  #take each line and splits it into its elements
    for word in word:
        if word not in dictionary_words:
            dictionary_words[word] = 1   #adds key and assigns value if  first entry
        else :
            dictionary_words[word] = dictionary_words[word] + 1  #increases the count by 1 for key

if 'Python' in dictionary_words:
    print('True')
else:
    print('False')
