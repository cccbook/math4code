If  = lambda c:lambda a:lambda b:a if c else b
Max = lambda a: lambda b: If(a>b)(a)(b)
Min = lambda a: lambda b: If(a<b)(a)(b)

If_n = lambda n: lambda cond: lambda a: lambda b: a(n) if cond else b(n)
Fibonacci = lambda n: If_n(n)(n<2)(lambda n:n)(lambda n:Fibonacci(n-1)+Fibonacci(n-2))
n = 5
print('n=', n, 'If(n>3)("n>3")("n<=3")=', If(n>3)("n>3")("n<=3"))
n = 1
print('n=', n, 'If(n>3)("n>3")("n<=3")=', If(n>3)("n>3")("n<=3"))
print('Max(3,5)=', Max(3)(5))
print('Min(3,5)=', Min(3)(5))
print('Fibonacci(8)=', Fibonacci(8))
