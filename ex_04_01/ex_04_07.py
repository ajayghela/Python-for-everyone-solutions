"""
Exercise 4.7: Rewrite the grade program from the previous chapter using a function called computegrade
that takes a score as its parameter and returns a grade as a string.

"""

score = input("Enter score: ")

def computegrade (Score) :
    if score > 1:
       return("Bad score")
    elif score >= 0.9:
       return("A")
    elif score >= 0.8:
       return("B")
    elif score >= 0.7:
       return("C")
    elif score >= 0.6:
       return("D")
    elif score < 0.6:
       return("F")


try:
   score = float(score)
except:
   print("Bad Score")
   quit()

score = computegrade(score)
print("grade:", score)
