import * as B from 'https://deno.land/x/bigint/mod.ts'

console.log('B.randomBigInt(100)=', B.randomBigInt(100)) // generate a bigint with 100 digits

let p = 2168800793765936984686210592376586144510492082787099063028443587189966802549907290827442681374512259n
console.log(`isPrime(${p})=`, B.isPrime(p)) // p is a prime

console.log('isPrime(97)=', B.isPrime(97n)) // 97 is a prime
console.log('isPrime(99)=', B.isPrime(99n)) // 99 is a prime

for (let i=0; i<5; i++) {
    let r = B.randomPrime(50)
    console.log(`${r} is a prime`)
}

console.log('modPow(3n,4n,5n)=', B.modPow(3n, 4n, 5n)) // 3*5 mod 4 == 1
console.log('modInv(5n,17n)=', B.modInv(5n,17n)) // 5*7 mod 17 == 1
