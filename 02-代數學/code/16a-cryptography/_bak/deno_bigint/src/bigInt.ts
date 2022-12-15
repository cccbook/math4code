import * as lib6 from 'https://deno.land/x/lib6/mod.ts'

export function randomBigInt(len: number) {
  return BigInt(lib6.randomBaseStr(10, len))
}

export function modPow(b: bigint, e: bigint, n: bigint): bigint {
  b = b % n
  let r = 1n
  while (e > 0) {
    if ((e % 2n) === 1n) {
      r = r * b % n
    }
    e = e / 2n
    b = b ** 2n % n
  }
  return r
}

// 參考 -- https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
// gcd(a,b) = ri = a*si+b*ti
// gcd(e,N) =  1 = e*si+N*ti
//             1 = e*si mod N  => si=d 是 e 的 modInverse
export function extEuclid(a: bigint, b: bigint) {
  let [si, s] = [1n, 0n] // let si = 1n, s = 0n // let [si,s] = [1n,0n]
  let [ti, t] = [0n, 1n] // let ti = 0n, t = 1n // let [ti,t] = [0n,1n]
  let [ri, r] = [a, b] // let ri = a, r = b   // let [ri,r] = [a,b]
  if (b === 0n)
    return [1n, 0n, a]
  else {
    while (r != 0n) {
      let q = ri / r
      let rt = r; r = ri - q * rt; ri = rt; // [ri, r] = [r, ri-q*r]
      let st = s; s = si - q * st; si = st; // [si, s] = [s, si-q*s]
      let tt = t; t = ti - q * tt; ti = tt; // [ti, t] = [t, ti-q*t]
    }
  }
  return [si, ti, ri]
}

// https://ithelp.ithome.com.tw/articles/10236425
// 擴展歐幾里得算法的等效公式：ax+by = gcd(a,b)。
// gcd(a,b)=ri=1=a*si+b*ti
// gcd(x,N)=1=x*si+N*ti   => x*si=1 mod N
export function modInv(x:bigint, N:bigint) {
  let [si] = extEuclid(x, N)
  return (si+N)%N
}

// ===================== millerRabinPrime() test======================
// Fermat 定理：若 n 是質數，則 a^{n-1} mod n = 1
// Pseudo Prime 偽質數：若 a^{n-1} mod n = 1
export function decompose(m: bigint) { // m=2^t * u
  let u = m
  for (var t = 0n; u % 2n == 0n; u = u / 2n) {
    t++
  }
  return { t, u }
}

export function witness(a: bigint, n: bigint) {
  let { t, u } = decompose(n - 1n)
  let x = modPow(a, u, n)
  for (let i = 1n; i <= t; i++) {
    let xn = modPow(x, 2n, n)
    if (xn == 1n && x != 1n && x != n - 1n)
      return true
    x = xn
  }
  if (x != 1n) return true
  return false
}

// 這個太慢，所以用隨機的 millerRabinPrime() 檢驗
export function isPrimeSlow(p:bigint) {
  for (let i = 2n; i * i <= p; i++) {
    if (p % i === 0n) return false;
  }
  return true;
}

export function millerRabinPrime(n: bigint, s: bigint) {
  let len = n.toString().length
  for (let i = 1n; i <= s; i++) {
    let a = randomBigInt(len) % n
    if (witness(a, n))
      return false
  }
  return true
}

export function isPrime(n: bigint) {
  return millerRabinPrime(n, 10n)
}

export function randomBigMayPrime(len: number) {
  return BigInt(lib6.randomBaseStr(10, len-1)+lib6.randomChar('1379'))
}

// 找不到就傳回 null
export function randomPrime(len: number, maxLoops: number = 9999999) {
  var r = null, failCount=0
  for (let i = 0; i < maxLoops; i++) {
    r = randomBigMayPrime(len)
    if (isPrime(r)) {
      break
    } else {
      failCount ++
      // console.log('failCount=', failCount)
    }
  }
  return r
}

