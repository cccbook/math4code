# bigint -- A library for big integer

## Import

```js
import * as B from 'https://deno.land/x/bigint/mod.ts'
```

## Example

```js
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

```

## run

```
$ deno run bigint1.js
B.randomBigInt(100)= 8123067927321377708965209884739259839090041701429788931690691759797050743782128790049119786118035617n
isPrime(2168800793765936984686210592376586144510492082787099063028443587189966802549907290827442681374512259)= true
isPrime(97)= true
isPrime(99)= false
92158026240608273170326567321316506895567322226319 is a prime
55247335046238853599623698640325239481442525299967 is a prime
82548719741844654149361556556649113111249681261111 is a prime
17089656126155545550317137708462525989105979874391 is a prime
70837166573493351149941100082901144367281693068067 is a prime
modPow(3n,4n,5n)= 1n
modInv(5n,17n)= 7n
```