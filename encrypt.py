from ecdsa import SigningKey, SECP256k1

# Generating a private key
sk = SigningKey.generate(curve=SECP256k1)
print("Private key generated:", sk.to_string().hex())

# Generating a public key
vk = sk.verifying_key
print("Public key generated:", vk.to_string().hex())

# Signing a message
message = b"Not your Keys, not your Coins!"
signature = sk.sign(message)
print("Message signature:", signature.hex())

# Verifying the signature
assert vk.verify(signature, message)

# If the assertion is successful, the script will continue executing
print("Signature verification successful!")
