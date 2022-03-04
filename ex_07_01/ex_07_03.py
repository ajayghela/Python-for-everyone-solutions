"""
Exercise  7.3: Sometimes when programmers get vored or want to have a bit of
fun, they adda harmless Easter Egg to their program. Modify the program that
prompts the user for a file name so that is prints a funny message when the
the user types in the exact file name "na na boo boo". the program should
behave normally for all other files which exist and don't exit. Here is a
sample execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

"""
count = 0
total = 0
fname = input('Enter the file name: ')  #promt for file name
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit() 
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
