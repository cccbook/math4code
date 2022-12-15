import math

def f(n):
    r = 1
    for i in range(1,n+1):
        r*=i
    return r

def sin(x, n):
    r = 0
    for i in range(0,n):
        r += (x**(2*n+1))*((-1)**n)/fact(2*n+1)
    return r

print('sin(pi/6)=', sin(math.pi/6, 10))
