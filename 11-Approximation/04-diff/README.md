# diff.py

x**5 的 n 次微分

```
x = 2
f(x) = x**5 =32
f'(x) = 5x**4 = 80
f''(x) = 5*4*x**3 = 160
f3(x) = 5*4*3*x**2 = 240
f5(x) = 5*4*3*2*x = 240
```

但是算出來卻是

```
$ python diff.py
df(x**5, pi/4)= 80.00080000485355
dfn(x**5, 2, 0)= 32
dfn(x**5, 2, 1)= 80.00080000485355      
dfn(x**5, 2, 2)= 160.00235802948737     
dfn(x**5, 2, 3)= 241.58453015843403     
dfn(x**5, 2, 4)= 710542.7357601002      # 這裡開始有嚴重錯誤
dfn(x**5, 2, 5)= -284217094304.04004    
dfn(x**5, 2, 6)= 7.8159700933611e+16    
dfn(x**5, 2, 7)= -1.9184653865522697e+22
dfn(x**5, 2, 8)= 4.405364961712619e+27  
dfn(x**5, 2, 9)= -9.521272659185337e+32 
```