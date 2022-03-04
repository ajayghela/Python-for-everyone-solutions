"""
Exercise 12.3: Use urllib to replicate the previous exercise of 
(1) retrieving the document from a URL, 
(2) displaying up to 3000 characters, 
and (3) counting the overall number of characters in the document. 
Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

"""

import urllib.request, urllib.parse, urllib.error

url = input("Enter a URL:")
fhand = urllib.request.urlopen(url).read() #'http://data.pr4e.org/romeo.txt')

content = fhand.decode()

print(content[:3000])
print(len(content))

#url = input("Enter a URL:")
#fhand = urllib.request.urlopen(url) #'http://data.pr4e.org/romeo.txt')

#count = 0
#for line in fhand:
    #words = line.decode().strip()
    #print(words)
    #for word in words:
        #count += 1

#print(words[:3000])
#print(count)
