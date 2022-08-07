import random
import time

def gen_random_list(n):
    assert(n>0)
    l = [random.randint(0, 10*n) for i in range(n)]    
    return l
    
#1
start_time = time.perf_counter()
def linear_search(s,k):
    for i in range(len(s)):
        if s[i] == k:
            return i
    return -1
spent_time = time.perf_counter() - start_time

#2
def binary_search(s,k):
    s.sort()
    first = 0
    last = len(s)-1
    while(first <= last):
        mid = (first + last) // 2
        if s[mid] == k:
            return mid
        else:
            if s[mid] < k:
                first = mid + 1
            else:
                last = mid - 1
    return -1

if __name__ == '__main__':
    l = gen_random_list(100000000)
    print(l)
    k = -5
    print(linear_search(l,k))
    print("Time spent calling linear search: ", spent_time)