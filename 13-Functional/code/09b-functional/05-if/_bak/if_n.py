If = lambda cond, a, b: a if cond else b
Max = lambda a,b: If(a>b, a, b)
Min = lambda a,b: If(a<b, a, b)

# 如果 Fibonacci 用 If 而非 If_n, 那麼 Fibonacci(n-1) 會馬上運算，結果就是 8=>7=>....0=>-1=>-2=>.... 當掉
If_n = lambda n, cond, a, b: a(n) if cond else b(n)
Fibonacci = lambda n: If_n(n, n<2, lambda n:n, lambda n:Fibonacci(n-1)+Fibonacci(n-2))

print('Max(3,5)=', Max(3,5))
print('Min(3,5)=', Min(3,5))
print('Fibonacci(8)=', Fibonacci(8))

