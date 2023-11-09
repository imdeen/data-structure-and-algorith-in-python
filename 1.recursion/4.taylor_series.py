def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1)*n


def power(x, y):
    if y == 0:
        return 1
    else:
        return power(x , y-1)*x
# print(power()) 

p = 1
f = 1
def taylor(x,n):
    global p, f
    if n == 0:
        return 1
    else:
        r = taylor(x,n-1) 
        p = p*x
        f = f*n
        return r + p/f
    
print(taylor(3,4))




#horner's rules

#iterative version
def horner_iterative(x,n):
    s = 1
    if n == 0:
        return s
    else:
        while n > 0:
            s = 1 + x/n*s
            n = n-1
        return s
        
print(horner_iterative(3,4))

#recusive version
s = 1
def horner_recursive(x,n):
    global s
    if n == 0:
        return s
    else:
        s = 1 + x/n*s
        return horner_recursive(x, n-1)
print(horner_recursive(3,4))






