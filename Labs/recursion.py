
def recursive_factorial(n):
    """
    Computes the factorial of n using a recursive approach
    
    n! = n * (n-1)!
    0! = 1! = 1
    
    This function does not do any error checking.

    Parameters
    ----------
    n : int

    Returns
    -------
    The factorial of n

    """ 
    
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * recursive_factorial(n-1)


def recursive_fibonacci_number(n):
    """
    Computes the n-th number in the Fibonacci sequence using a recursive definition of the Fibonacci number

    F(0)= 0 
    F(1) = 1
    F(n) = F(n-1) + F(n-2)  for n > 1
    
    This function does not do any error checking.

    Parameters
    ----------
    n : int


    Returns
    -------
    The n-th number in the Fibonacci sequence

    """

    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci_number(n-1) + recursive_fibonacci_number(n-2)    
    
  
def recursive_exponentiation(a, n):
    """
    Returns a^n (a raised to the power of n).

    This function does not do any error checking.

    Parameters
    ----------
    a : float
        base.
    n : int
        exponent (must be >= 0).

    Returns
    -------
    a raised to the power of n
    
    """    
    if n == 0:
        return 1
    else:
        return a * recursive_exponentiation(a, n-1)


def recursive_list_length(l):
    """
    Returns the length of a list using a recursive implementation.
    
    The length of the empty list [] is 0
    Otherwise the length is 1 + the length of the list without the first element
    
    Of course there's a builtin function doing that already, but that's not the point.

    l[1:] is the list without the first element. This is also called the tail of the list

    Parameters
    ----------
    l : list
        

    Returns
    -------
    Lenght of the list.

    """
    if l == []:
        return 0
    else:
        return 1 + recursive_list_length(l[1:])    # l[1:] is the list with the first element removed


def recursive_max_list(l):
    """
    Determines the largest element in a list using a recursive formulation.
    
    If the list has just one element, then that element is the maximum.
    Otherwise the maximum the largest between the first element and the maximum 
    of the list with the first element removed.

    And of course, there's a built in function that does this already...

    This function does not do any error checking.

    Parameters
    ----------
    l : list
        non empty list of integers.

    Returns
    -------
    The maximum element in the list.

    """
    if recursive_list_length(l) == 1: # just one element?
        return l[0]
    else:
        return max(l[0], recursive_max_list(l[1:]))


def recursive_list_append(l1, l2):
    """
    Returns the list obtained appending l2 to l1.
    
    If l2 is the empty list, then the result is l1. Otherwise the result is
    obtained appending to l1 the first element of l2 end then appending
    the rest of l2.
    
    The implementation should be more sophisticated to deal with references, but 
    we keep it simple.
    
    This function uses the *l notation to "unpack" the elements in a list

    Parameters
    ----------
    l1 : list

    l2 : list
    

    Returns
    -------
    List l

    """
    if l2 == []:
        return l1
    else:
        return recursive_list_append([*l1, l2[0]], l2[1:])



if __name__ == '__main__':
    n = int(input('Enter a natural number: '))
    f = recursive_factorial(n)
    print('Its factorial is', f)
    fib = recursive_fibonacci_number(n)
    print('Its fibonacci is', fib)
    base = float(input('Enter a base (real number): '))
    exponent = int(input('Enter an exponent (natural number): '))
    exp_res = recursive_exponentiation(base, exponent)
    print(base, 'to the power of', exponent, 'is', exp_res)
    
    l1 = [1,5,7,9,6]
    print('List l1 is', l1)
    len_list = recursive_list_length(l1)
    print('Its length is', len_list)
    max_el = recursive_max_list(l1)
    print('The maximum element is', max_el)
    l2= [67,45,23]
    print('List l2 is', l2)
    conc = recursive_list_append(l1, l2)
    print('The two list appended are', conc)