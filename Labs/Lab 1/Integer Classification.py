#This is the Integer Classification practice
"""
This will ask the user for their favorite number
and tell them whether or not it is odd or even
"""
num = int(input("What is your favorite number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
