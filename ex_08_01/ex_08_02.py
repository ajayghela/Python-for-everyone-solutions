"""
Exercise  8.2: Figure out which line of the above program is still not properly
guarded. See if you can construct a text file which causes the program to fail
and then modify the program so that the line is properly guarded and test it to
make sure it handles your new text file.

"""

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    #print('line:', line)  <-- debugging purposes
    words = line.split()
    #print('words:', words)
    #Guardian statements:
    if len(words) < 3:     #to ensure the line has at least 3 words for our print at the end)
        continue
    if words[0] != 'From':
        #print('ignore')
        continue
    print(words[2])
