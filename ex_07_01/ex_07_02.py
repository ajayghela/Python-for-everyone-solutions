"""
Exercise  7.2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence:0.8475
When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
the line to extract the floating-point number on the line. count these lines
and then compute the total of the spam confidence values from these lines.
When you reach the end of the file, print out the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.

"""

count = 0
total = 0
fname = input('Enter the file name: ')  #prompt for file name
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):  #pulls line
        count = count + 1
        character = line.find(':')          # find the character :
        num = line[character+1:]            # finds number after colon. "colon number = line[character+1:].strip()" ... removes all text except number
        num = float(num)                    #float
        total = total + num
        #print(num)
        #print(total)
        #print(count)    <<<- print used to check code
        continue

average = total / count
print('Average spam confidence: ', average)
