A = set(['a','b','c','d'])
B = set([1,2,3,4,5,6])
f = set([('a',1),('b',1),('c',5),('d',4)])

print('Domain A')
print(A)
print(' ')
print('Codomain B')
print(B)
print(' ')

print('Graph of the function')
print(f)
print(' ')

#====================================================================

def is_surjective(A, B, f):
    for element in f:
        a = element[1]
        for other in f:
            if other != element:
                aprime = other[1]
                if a == aprime :
                    return False
    return True

check = is_surjective(A, B, f)
if check == True:
    print("Function f is surjective")
else:
    print("Function f is not surjective")