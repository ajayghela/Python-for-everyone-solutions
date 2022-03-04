"""
Exercise  8.1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list
that contains all but the first and last e lements.

"""
def chop(t):
    del t[0]        #removes the first element
    del t[-1]       #removes the last element

def middle(t):
    new = t[1:]     #stores all but the first element
    del new[-1]     # removes the last element
    return new

order = [1, 2, 3, 4]
order2 = [1, 2, 3, 4]

chop_list = chop(order)
print(order)
print(chop_list)

middle_list = middle(order2)
print(order2)
print(middle_list)
