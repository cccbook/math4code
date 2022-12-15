var crypto = require('crypto')

# 加密
def encrypt(algorithm, key, plainText) :
    var list = []
    var encrypter = crypto.createCipher(algorithm, key)
    list.push(encrypter.update(plainText, 'binary', 'hex'))
    list.push(encrypter.final('hex'))
    return list.join('')


# 解密
def decrpyt(algorithm, key, cipherText) :
    var list = []
    var decrypter = crypto.createDecipher(algorithm, key)
    list.push(decrypter.update(cipherText, 'hex', 'binary'))
    list.push(decrypter.final('binary'))
    return list.join('')


 key = 'adsjfa@#!(Oxxay'
 algorithm = 'aes-128-cbc'
 sendText = 'This is the plain text !'
print('sendText   = ', sendText)
 cipherText = encrypt(algorithm, key, sendText)
print('cipherText = ', cipherText)
 recvText = decrpyt(algorithm, key, cipherText)
print('recvText   = ', recvText)
