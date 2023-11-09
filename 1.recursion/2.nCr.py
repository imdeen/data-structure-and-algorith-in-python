#nCr using factorial

#recursive factorial function
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1)*n
    
#iterative factorial function
def fac(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res



def combination_fact(n,r):
    x = fact(n)
    y = fact(r)*fact(n-r)
    return x/y
    


#recursive combination formulae(see pascal triangle for neat explaination)
def combination_recursion(n,r):
    if r == 0 | n == r:
        return 1
    else:
        return combination_fact(n-1,r-1) + combination_fact(n-1,r) 
    

