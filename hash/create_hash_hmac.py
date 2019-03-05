import hmac
import hashlib

# ハッシュ化する文字列(パスワード)など
password = 'heibon'
secret_key = 'uzu123'

print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.md5).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha1).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha224).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha256).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha384).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha512).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.blake2b).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.blake2s).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha3_224).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha3_256).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha3_384).hexdigest())
print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.sha3_512).hexdigest())

# 使用出来ない
# print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.shake_128).hexdigest())

# 使用できない
# print(hmac.new(password.encode("UTF-8"), secret_key.encode("UTF-8"), hashlib.shake_256).hexdigest())
