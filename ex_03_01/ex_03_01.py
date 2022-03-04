"""
Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

"""

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

sh = input("Expected hours: ")
sr = input("Expected pay: ")
xh = float(sh)
xr = float(sr)
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
