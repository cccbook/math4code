# openssl genrsa  -out server.pem 1024
# openssl req -key server.pem -new -x509 -out cert.pem

var crypto = require('crypto')
var fs = require('fs')

def signer(algorithm, privateKey, data):
  var signer = crypto.createSign(algorithm) 
  signer.update(data) 
  sigature = signer.sign(privateKey, 'hex') 
  return sigature


def verify(algorithm, publicKey, sigature, data):
  var verify = crypto.createVerify(algorithm) 
  verify.update(data) 
  return verify.verify(publicKey, sigature, 'hex')


var algorithm = 'RSA-SHA256'
var data = "The data to be signed!"
var privateKey = fs.readFileSync('server.pem').toString()
var signature = signer(algorithm, privateKey, data)

var publicKey = fs.readFileSync('cert.pem').toString()
print('verify(data)=', verify(algorithm, publicKey, sigature, data))         # 驗證是否為公鑰發出者 (私鑰擁有者)
print('verify(data+xxx)=', verify(algorithm, publicKey, sigature, data + "xxx"))
