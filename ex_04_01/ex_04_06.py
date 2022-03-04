"""
Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime 
and create a function called computepay which takes two parameters (hours and rate).

"""

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours,rate) :
    #print ("in computepay", hours, rate)
    if hours > 40 :
       reg = hours * rate
       otp = (hours - 40.0) * (rate * 0.5)
       pay = (reg + otp)
    else:
       pay = hours * rate
    #print("returning pay", pay)
    return pay

sh = input("Expected hours: ")
sr = input("Expected pay: ")
xh = float(sh)
xr = float(sr)

xP = computepay(xh,xr)

print("Pay:", xP)
