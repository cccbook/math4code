# 參考： [維基百科:迪菲-赫爾曼密鑰交換](https://zh.wikipedia.org/wiki/%E8%BF%AA%E8%8F%B2-%E8%B5%AB%E7%88%BE%E6%9B%BC%E5%AF%86%E9%91%B0%E4%BA%A4%E6%8F%9B)
Alice = {'g':5, 'p':23, 'a':6} 
Bob   = {'b':15} 

def mpower(a, n, p):
    r = 1
    for _ in range(n):
        r = (r * a) % p
    return r

Alice['send'] = def(receiver):
    g, p, a = Alice
    A = mpower(g, a, p)
    receiver.receive(Alice, g, p, A)


Alice.receive = def (sender, B) :
   :g, p, a = Alice
  self.K = mpower(B, a, p)


Bob.receive = def (sender, g, p, A) :
   b = Bob.b
   B = mpower(g, b, p)
  self.K = mpower(A, b, p)
  Bob.send(sender, B)


Bob.send = def (receiver, B) :
  receiver.receive(Bob, B)


Alice.send(Bob)

print('Alice.K = %d', Alice.K)
print('Bob.K   = %d', Bob.K)
