""""
Exercise 5.2: Write another program that prompts for a list of numbers as above 
and at the end prints out both the maximum and minimum of the numbers instead of the average.

"""

num = 0
tot = 0.0
largest = None
smallest = None

while True:
    n = input('Enter a Number:')
    if n == 'done' :
        break
    try:
        fval = int(n)
    except:
        print('Invalid Input')
        continue
    #print(n)
    num = num + 1
    tot = tot + fval
    for i in range(fval):
        if largest is None or fval > largest:
            largest = fval
    for ii in range(fval):
        if smallest is None or fval < smallest:
            smallest = fval


#print('all done')
print(tot , num, 'smallest: ', smallest, 'largest: ', largest)
