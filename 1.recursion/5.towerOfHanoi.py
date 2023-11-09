def TOH(n,A,B,C):
    if n > 0:
        TOH(n-1,A,C,B)
        print(A, end=" ")
        print("to", end=" ")
        print(B )
        TOH(n-1,B,A,C)

TOH(6,1,2,3)