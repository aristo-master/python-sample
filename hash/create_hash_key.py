import hashlib

# ハッシュ化する文字列(パスワード)など
password = 'heibon'

# 秘密鍵
secret_key = 'uzu123'

print(hashlib.md5((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha1((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha224((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha256((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha384((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha512((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.blake2b((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.blake2s((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha3_224((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha3_256((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha3_384((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.sha3_512((password + secret_key).encode("UTF-8")).hexdigest())
print(hashlib.shake_128((password + secret_key).encode("UTF-8")).hexdigest(64))
print(hashlib.shake_256((password + secret_key).encode("UTF-8")).hexdigest(64))
