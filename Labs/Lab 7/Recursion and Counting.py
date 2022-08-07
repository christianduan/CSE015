# This is the code to find a value with a n-th value recursively
def compute_f(n):
    if n == 0:
        return 2
    else:
        return compute_f(n-1)+2

n = int(input("Please enter a value for n: "))

answer = compute_f(n)

print (answer)

# List for the count_instances() function
L =[2, 3, 1, 4, 2, 3, 1, 5, 7, 2]

# Function to find the instance of a number in the list above
def count_instances(L, x):
    if L == []:
        return 0
    if L[0] == x:
        return 1 + count_instances(L[1:], x)
    else:
        return 0 + count_instances(L[1:], x)

print (count_instances(L, 0))