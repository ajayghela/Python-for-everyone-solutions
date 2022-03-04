"""
Exercise 3.2: Rewrite your pay program using try and except so that your
program handles non-numerical input gracefully by printing a message and
exiting the program. The folowing shows two executions of the program:
Enter Hours: 20
Enter Rate : nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

"""

sh = input("Expected hours: ")
sr = input("Expected pay: ")
try:
   xh = float(sh)
   xr = float(sr)
except:
   print("Error, please enter numeric input")
   quit()
if xh > 40 :
   #print("Overtime")
   reg = xh * xr
   otp = (xh - 40.0) * (xr * 0.5)
   #print(reg,otp)
   xP = (reg + otp)
else:
   #print("Regular")
   xP = xh * xr
print("Pay:", xP)
