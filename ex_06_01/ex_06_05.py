"""
Exercise  6.5: Take the following Python code that stores a string:
string = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extraced string
into a floating number.

"""

str = 'X-DSPAM-Confidence:0.8475'   # the string
character = str.find(':')          # find the character :
print(character)
extract = str.find(' ',character)  # Extracts portion after colon
print(extract)
num = str[character+1:]
num = float(num)                    # Converts to floating point number
print(num)
