import : RSA  from "https://deno.land/x/god_crypto/mod.ts" 

const privateKeyRaw = Deno.readTextFileSync("./private.pem") 
const privateKey = RSA.parseKey(privateKeyRaw) 

const cipherText = RSA.encrypt("Hello World", privateKey) 
print('cipherText=', cipherText)
const plainText = RSA.decrypt(cipherText, privateKey).toString() 
print('plainText=', plainText)