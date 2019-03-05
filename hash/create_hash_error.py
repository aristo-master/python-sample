import hashlib

# ハッシュ化する文字列(パスワード)など
password = 'heibon'

hash = hashlib.sha1(password.encode("UTF-8")).hexdigest()

# 正常 472399b45c283b5c9fadc6611190450c2b4fe542
print(hash)

print(hashlib.sha1(password.encode("UTF-8")).hexdigest())
print(hashlib.md5(password.encode("UTF-8")).hexdigest())
print(hashlib.sha224(password.encode("UTF-8")).hexdigest())
print(hashlib.sha256(password.encode("UTF-8")).hexdigest())
print(hashlib.sha384(password.encode("UTF-8")).hexdigest())
print(hashlib.sha512(password.encode("UTF-8")).hexdigest())
print(hashlib.blake2b(password.encode("UTF-8")).hexdigest())
print(hashlib.blake2s(password.encode("UTF-8")).hexdigest())
print(hashlib.sha3_224(password.encode("UTF-8")).hexdigest())
print(hashlib.sha3_256(password.encode("UTF-8")).hexdigest())
print(hashlib.sha3_384(password.encode("UTF-8")).hexdigest())
print(hashlib.sha3_512(password.encode("UTF-8")).hexdigest())
print(hashlib.shake_128(password.encode("UTF-8")).hexdigest(64))
print(hashlib.shake_256(password.encode("UTF-8")).hexdigest(64))
