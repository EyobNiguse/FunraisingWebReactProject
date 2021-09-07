import hashlib
hash_object = hashlib.sha1(bytes("helloadmin", 'utf-8'))
hashed_password = hash_object.hexdigest()
print(hashed_password)