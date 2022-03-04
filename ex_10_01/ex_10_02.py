"""
Exercise  10.2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the "From" line by finding
the time string and then splitting that string into parts using the colon
character. Once you have accumulated the counts for each hour, print out the
counts, one per line, sorted by hour as shown below.
Sample line: From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""

fname = input("Enter a File Name: mbox-short.txt")
 
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
except:
    print("File cannot be opened:', fname")
    exit()

fhand = open(fname)

dictionary_list = dict()
for line in fhand:
    if line.startswith("From "):
        #print(line)
        time = line.split()[5]
        #print(time)
        hour = time.split(':')[0]
        #print(hour)
        dictionary_list[hour] = dictionary_list.get(hour,0) + 1
    
#print(dictionary_list)

hr_list = list()

for key, val in list(dictionary_list.items()):
    hr_list.append((key, val))

hr_list.sort()
for key, val in hr_list:
    print(key,val)








        

