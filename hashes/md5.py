from hashlib import md5, sha256

print(md5(b'hello').hexdigest())
print(sha256(b'hello').hexdigest())
