import sympy as sp
a = sp.ones(4)
for i in range(a.shape[0]): a[i,i]=3
D=a.det(); print("D=", D)
