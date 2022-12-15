import * as T from 'https://deno.land/x/tdd/mod.ts'
import * as B from '../mod.ts'

Deno.test("bigint", () => {
  const len = 500
  T.isType(B.randomBigInt(len), 'bigint')
  console.log('B.isPrime(97n)=', B.isPrime(97n))
  // T.ok(B.isPrime(97n))
  T.ok(!B.isPrime(99n))
  let p = 2168800793765936984686210592376586144510492082787099063028443587189966802549907290827442681374512259n
  T.ok(B.isPrime(p))
  for (let i=0; i<2; i++) {
      T.ok(B.isPrime(B.randomPrime(len)))
  }
  T.eq(B.modPow(3n, 4n, 5n), 1n)
  T.eq(B.modInv(5n,17n), 7n)
})

