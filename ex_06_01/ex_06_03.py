"""
Exercise 6.3: Encapsulate this code in a function named count, and generalize
it so that it accepts the string and the letter as arguments.

"""

def count(w,l):

    count = 0

    for i in w:
        if i == l:
            count = count + 1
    print(count)

word = input("Enter a string: ")
letter = input("Enter a letter: ")
count(word,letter)
