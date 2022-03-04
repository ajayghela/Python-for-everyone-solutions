"""
Exercise 5.1: Write a program which repeatedly reads numbers until the user enters "done". 
Once "done" is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, detect their mistake using try and except 
and print an error message and skip to the next number.

"""

num=0
tot=0.0
#Start by establishing my variables and establish my input
#first is the line for reading the number, then the line for "done" and print
#then  the try and except

while True:
    sval = input('Enter a Number:')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    #print(sval)
    num = num + 1
    tot = tot + fval


#print('all done')
print(tot,num,tot/num)
