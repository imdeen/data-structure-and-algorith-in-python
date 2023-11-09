#fatorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#tail recursion
def tail_recusion(n):
    if n > 0:
        tail_recusion(n-1)
        print(n , end=' ')

#rested recursion
def nested_recursion(n):
    if n > 100:
        return n - 10
    else:
        return nested_recursion(nested_recursion(n+11))



#tree recursion
def tree_recusion(n):
    if n > 0:
        print(n, end='')
        tree_recusion(n-1)
        tree_recusion(n-1)



#exponent
def exponent(x,y):
    if y == 0:
        return 1
    else: 
        return exponent(x , y-1)*x
print(exponent(2,4))


