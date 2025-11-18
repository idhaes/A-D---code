def faculteit(n):
    if n > 13:
        return "invoer te groot"
    return hulp_faculteit(n, 1)

def hulp_faculteit(n, result):
    if n == 0:
        return result
    return hulp_faculteit(n-1, result * n) #waarde moet doorgeven worden naar boven!

for i in range(int(input())):
    print(faculteit(int(input())))