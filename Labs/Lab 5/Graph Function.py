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

def is_a_graph(A,B,f):
    for element in f:
        b = element[0]
        for other in f:
            if other != element: 
                bprime = other[0]
                if b == bprime:
                    return False
    return True  

check1 = is_a_graph(A, B, f)
if check1 == True:
    print('')
    print('Function f is a graph')
else:
    print(' ')
    print('Function f is not a graph')