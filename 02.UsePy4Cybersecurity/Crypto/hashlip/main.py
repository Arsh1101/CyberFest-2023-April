import hashlib

message = 'This is a message to hash.'.encode('utf-8')
hash_object = hashlib.sha256(message)
# hexadecimal string representing the hash
hash_hex = hash_object.hexdigest()

print(hash_hex)
