import hashlib, binascii
import sys

text = 'hello'
data = text.encode("utf8")

sha256hash = hashlib.sha256(data).digest()
print("SHA-256:   ", binascii.hexlify(sha256hash))

sha3_256 = hashlib.sha3_256(data).digest()
print("SHA3-256:  ", binascii.hexlify(sha3_256))

blake2s = hashlib.new('blake2s', data).digest()
print("BLAKE2s:   ", binascii.hexlify(blake2s))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160))



"""
Hashing using sha3_256
"""
data = 'Hello World'
data = data.encode('utf-8') # convert to bytes
print(data)
hash = hashlib.sha3_256(data).hexdigest() # hash the data

print(hash)

# sys.exit()

"""
Hashing using sha256
"""
hash = hashlib.sha256(data).hexdigest()
print(hash)

"""
Hashing using sha1
"""
hash = hashlib.sha1(data).hexdigest()
print(hash)

"""
Hashing using md5
"""
hash = hashlib.md5(data).hexdigest()
print(hash)

# print(cryptography)
