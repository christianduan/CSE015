A = set(['a', 'b', 'c', 'd'])
B = set([1, 2, 3, 4, 5, 6])
f = set([('a', 3), ('b', 4), ('c', 5), ('d', 1)])
g = set([('b', 4), ('a', 3), ('d', 1), ('c', 5)])
h = set([(2, 'bird'), (4, 'cat'), (3, 'dog'), (5, 'fish')])

#======================================================
def equal_functions(f, g):
    print('Function f:')
    print(f)
    print('Function g:')
    print(g)
    print(' ')

    if f == g:
        return True
    else:
        return False

check1 = equal_functions(f, g)
if check1 == True:
    print('Functions f and g are equal.')
    print(' ')
else:
    print('Functions f and g are not equal.')
    print(' ')

#======================================================
def is_partial_function(A, f):
    print('Set A:')
    print(A)
    print('Function f:')
    print(f)
    print(' ')

    count = 0
    b = len(A)
    for element in f:
        a = element[0]

    i = len(a)
    while count != i:
        count = count + 1

    if count < b:
        return True

check2 = is_partial_function(A, f)
if check2 == True:
    print('Function f is a partial function of A.')
    print(' ')
else:
    print('Function f is not a partial function of A.')
    print(' ')

#======================================================
def composite_function(f, h):
    j = set({})
    for element in f:
        for item in h:
            if element[1] == item[0]:
                j.add((element[0], item[1]))
    print(f, h)
    print(' ')
    print("Composite function:")
    return j

print(composite_function(f, h))