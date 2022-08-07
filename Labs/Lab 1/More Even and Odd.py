#This is the More Even and Odd practice
"""
This will ask the user to input ten integers
and will return the largest odd number or it
will state 'There were no odd numbers' if there
were no odd numbers entered
"""
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
num4 = int(input('Enter a number: '))
num5 = int(input('Enter a number: '))
num6 = int(input('Enter a number: '))
num7 = int(input('Enter a number: '))
num8 = int(input('Enter a number: '))
num9 = int(input('Enter a number: '))
num10 = int(input('Enter a number: '))

if num1%2 == 0:
    num1 = 0  
else:
    num1 = num1 
if num2%2 == 0:
    num2 = 0 
else:
    num2 = num2
if num3%2 == 0:
    num3 = 0
else:
    num3 = num3 
if num4%2 == 0:
    num4 = 0
else:
    num4 = num4
if num5%2 == 0:
    num5 = 0
else:
    num5 = num5
if num6%2 == 0:
    num6 = 0
else:
    num6 = num6
if num7%2 == 0:
    num7 = 0
else:
    num7 = num7
if num8%2 == 0:
    num8 = 0
else:
    num8 = num8
if num9%2 == 0:
    num9 = 0 
else:
    num9 = num9 
if num10%2 == 0:
    num10 = 0  
else:
    num10 = num10

value = num1, num2, num3, num4, num5, num6, num7, num8, num9, num10
max = max(value)
if max ==0:
    print('There are no odd numbers.')
else: 
    print(max, 'is the largest odd number.')