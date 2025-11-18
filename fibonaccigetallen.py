def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    

#Tail Recursion
#def fib(n):
#    return fib_helper(n, 0, 1)

#def fib_helper(n, a, b):
#    if n == 0:
#        return a
#    return fib_helper(n-1, b, a+b)