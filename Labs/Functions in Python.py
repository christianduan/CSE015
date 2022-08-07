#This is the average function
def average(l):
    return sum(l)/len(l)

print(average([1, 2, 3, 4]))

print(' ')

#This is the perfect square function
def is_perfect_square(n):
    if n ** 0.5 % 1 == 0:
        return True
    else:
        return False

for i in range(10):
    print(i, is_perfect_square(i))

print(' ')

#This is the binary partition function
def binary_partition(A, B, C):
    if A & B == set() and A|B == C:
        return True
    else:
        return False

print(binary_partition({1, 2}, {3, 4}, {1, 2, 3, 4}))

print(' ')

#This is the generic partition function
def generic_partition(A, C):
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] & A[j] != set():
                return False
    tmp = set()
    for a in A:
        tmp = tmp|a
        if tmp != C:
            return False
        else:
            return True

print(generic_partition({1, 2}, {1, 2, 3, 4}))

print(' ')


#This is the cartesian product function
def cartesian_product(A, B):
    output = set()
    for a in A:
        for b in B:
            output.add((a, b))
    return output

print(cartesian_product({1, 2}, {3, 4}))

print(' ')

#This is the has duplicates function
def has_duplicates(l):
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                return True
    return False

print(has_duplicates([1, 2, 3, 5, 10, 20]))
print(has_duplicates([1, 2, 3, 3]))

def has_duplicates_2(l):
    if len(set(l)) == len(l):
        return False
    else:
        return True

print(has_duplicates_2([1, 2, 3, 5, 10, 20]))
print(has_duplicates_2([1, 2, 3, 3]))