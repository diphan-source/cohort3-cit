# import hashlib, binascii
# import sys

# text = 'hello'
# data = text.encode("utf8")

# sha256hash = hashlib.sha256(data).digest()
# print("SHA-256:   ", binascii.hexlify(sha256hash))

# sha3_256 = hashlib.sha3_256(data).digest()
# print("SHA3-256:  ", binascii.hexlify(sha3_256))

# blake2s = hashlib.new('blake2s', data).digest()
# print("BLAKE2s:   ", binascii.hexlify(blake2s))

# ripemd160 = hashlib.new('ripemd160', data).digest()
# print("RIPEMD-160:", binascii.hexlify(ripemd160))



# """
# Hashing using sha3_256
# """
# data = 'Hello World'
# data = data.encode('utf-8') # convert to bytes
# print(data)
# hash = hashlib.sha3_256(data).hexdigest() # hash the data

# print(hash)

# # sys.exit()

# """
# Hashing using sha256
# """
# hash = hashlib.sha256(data).hexdigest()
# print(hash)

# """
# Hashing using sha1
# """
# hash = hashlib.sha1(data).hexdigest()
# print(hash)

# """
# Hashing using md5
# """
# hash = hashlib.md5(data).hexdigest()
# print(hash)

# print(cryptography)
# utf-16
# utf-32


#  types of hash functions
# -sha 256
# -sha 3 256
# md5
# ripemd 160

# text = 'hello' #plain text 
# text = text.encode('utf-8') # convert to bytes  ------------------->  b'hello'
# hash = hashlib.sha256(text).hexdigest() # hash the data
# print(f"SHA-256: {hash}")

# hash = hashlib.sha3_256(text).hexdigest() # hash the data
# print(f"sha3_256: {hash}")

# hash = hashlib.new('blake2s', text).hexdigest() # hash the data
# print(f"blake2s: {hash}")

# hash = hashlib.new('ripemd160', text).hexdigest() # hash the data
# print(f"ripemd160: {hash}")

# hash = hashlib.md5(text).hexdigest() # hash the data
# print(f"md5: {hash}")


import hashlib 

data = 'Hello World'
data = data.encode('utf-8') # convert to bytes
hash = hashlib.sha3_256(data).hexdigest() # hash the data
print(hash)

digest -----> returns the hash value of the data (binary)
hexdigest -----> returns the hash value of the data (hexadecimal) string 