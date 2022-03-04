"""
Exercise  10.3: Write a program that reads a file and prints the letters in
decreasing order of frequency. Your program should convert all the input to
lower case and only count the letters a-z. Your program should not count
spaces, digits, puntuaction, or anything other than letters a-z. Find text
samples from several different languages and see how letter frequency varies
between languages. Compare your results with the tables at
wikipedia.org/wiki/Letter_frequencies

"""
import string

fname = input("Enter a File: mbox-short.txt")

try:
    if len(fname) < 1 : fname = "mbox-short.txt"
except:
    print("File cannot be opened:", fname)
    exit()

fhand = open(fname)
#text = fhand.read()
#print(text)

di_alpha = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('','',string.digits))
    line = line.lower()
    line = line.split()
    
    for word in line:
        for letter in word:
            di_alpha[letter] = di_alpha.get(letter, 0) + 1

#print(di_alpha)

alpha_list = list()
for k,v in list(di_alpha.items()):
    alpha_list.append((v,k))

alpha_list.sort(reverse=True)
for v,k in alpha_list:
    print(k,v)





    



