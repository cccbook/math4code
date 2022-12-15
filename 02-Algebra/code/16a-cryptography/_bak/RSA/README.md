# RSA

參考： https://en.wikipedia.org/wiki/RSA_(cryptosystem)

## rsa.js

```
PS D:\ccc\ccc109a\se\deno\alg\14-cryptography\RSA> deno run -A rsa.js
Check file:///D:/ccc/ccc109a/se/deno/alg/14-cryptography/RSA/rsa.js
cipherText= RawBinary(256) [
  158, 226, 217, 195, 176, 178, 132, 12, 86, 246, 122, 60, 69,  53,
  202, 124, 177, 167, 144, 129, 64, 143, 209, 135, 14, 111, 62,  69,
  115, 253, 149, 229, 243, 200, 29, 147, 18, 59, 82, 97, 201, 159,
  221, 15, 49, 122, 77, 72, 134, 31, 22, 22, 202, 68, 83, 236,
  252, 196, 231, 197, 30, 112, 211, 157, 71, 61, 234, 46, 255, 214,
  45, 1, 148, 84, 165, 100, 216, 154, 39, 171, 44, 106, 84, 242,
  212, 233, 214, 246, 43, 53, 169, 98, 62, 44, 163, 162, 83,  61,
  196,  10,
  ... 156 more items
]
plainText= Hello World
```


## simpleRSA.js

```
PS D:\ccc\ccc109a\se\deno\alg\14-cryptography\RSA> deno run simpleRsa.js
M1= [ 65, 22, 37, 18, 29 ]
E1= [ 2790, 2558, 1350, 2100, 1912 ]
M2= [ 65, 22, 37, 18, 29 ]
```

## 數學背景

1. n = pq       # p, q 均為質數
2. r = (p-1)(q-1)
3. 找一 e 與 r 互質，並解得 e 的反元素 d， e*d = -1 mod r

e 為公鑰，d 為私鑰

## 程序

1. Alice.broadcast(n, e)
2. Bob.sendTo(Alice, c)
  * c = m^e (mod n)  # m 為訊息
3. Alice.receiveFrom(Bob, c)
  * c^d =m (mod n)

c^d = m^:ed = m (mod N)

範例： 

```
p=61, q=53, n=61*53=3233, λ(3233)=lcm(61,53)=780

 e = 17 , compute d = 413

e*d = 1 mod λ(n)
17*413 = 1 mod 780
```

假如 Bob 要傳 m 給 Alice，則可以傳送 c=m^e (mod n) 這個密文，然後 Alice 透過下列方式解碼：

c^d = m^ed = m (mod n) 

