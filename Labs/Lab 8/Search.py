import random
import time

# Random list generator function
def gen_random_list(n):
    assert(n>0)
    l = [random.randint(0, 10*n) for i in range(n)]    
    return l

# Linear search function
def linear_search(s,k):
    i = 0
    n = len(s) - 1

    while i <= n and k != s[i]:
        i += 1
    if i <= n:
        return -1

# Binary search function
def binary_search(s, k):
    i = 0
    j = len(s)

    while i < j:
        # Finds the middle of the set
        m = (i + j)//2
        if k > s[m]:
            i = m + 1
        else:
            j = m
    if k == s[i]:
        I = i
    else:
        I = -1
    return I

# Linear search timer
print("Linear Search Times")
print("=================")
for i in range(9):
    l = gen_random_list(10**i)

    start_time = time.perf_counter()
    linear_search(l, -1)
    spent_time = time.perf_counter() - start_time

    print ("List length = 10^" + str(i))
    print(spent_time)
    print("-----------------")

# Binary search timer
print("Binary Search Times")
print("=================")
for i in range(9):
    l = gen_random_list(10**i)

    start_time = time.perf_counter()
    binary_search(l, -1)
    spent_time = time.perf_counter() - start_time

    print ("List length = 10^" + str(i))
    print(spent_time)
    print("-----------------")