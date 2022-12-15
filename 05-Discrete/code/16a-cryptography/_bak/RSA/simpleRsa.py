def mpower(a, n, p) :
   r = a
  for ( i=2  i<=n  i++) :
    r = (r * a) % p
  
  return r


var p = 61, q = 53, N = p*q # lcm(61,53)=780
 e = 17 , d = 413

# var p = 37, q = 67, N = p * q
#  e = 23, d = 

var M1 = [65, 22, 37, 18, 29]
var E1 = []
var M2 = []
for ( m of M1) :
   c = mpower(m, e, N)
  E1.push(c)
   m2 = mpower(c, d, N)
  M2.push(m2)


print('M1=', M1)
print('E1=', E1)
print('M2=', M2)
