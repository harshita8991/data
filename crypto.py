"""
Practical 4: Cryptography
Demonstrates encryption (symmetric + asymmetric), hashing and digital signatures.
Requires: pip install cryptography
"""
import hashlib
import os

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidSignature

message = b"Student ID: 12345 | Marks: 92 | Confidential"

print("=" * 60)
print("ORIGINAL MESSAGE:", message.decode())
print("=" * 60)

# ---------------------------------------------------------------
# 1. SYMMETRIC ENCRYPTION (AES-256-GCM) - same key encrypts/decrypts
# ---------------------------------------------------------------
print("\n[1] SYMMETRIC ENCRYPTION - AES-256-GCM")
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)
nonce = os.urandom(12)                       # unique per message
ciphertext = aesgcm.encrypt(nonce, message, None)
print("Ciphertext (hex):", ciphertext.hex())
decrypted = aesgcm.decrypt(nonce, ciphertext, None)
print("Decrypted       :", decrypted.decode())

# Tamper test: GCM detects any change to the ciphertext
tampered = bytearray(ciphertext)
tampered[0] ^= 1
try:
    aesgcm.decrypt(nonce, bytes(tampered), None)
except Exception:
    print("Tampered ciphertext rejected (integrity check works)")

# ---------------------------------------------------------------
# 2. ASYMMETRIC ENCRYPTION (RSA-2048 with OAEP)
# ---------------------------------------------------------------
print("\n[2] ASYMMETRIC ENCRYPTION - RSA-2048")
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
oaep = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None,
)
short_msg = b"Secret: meet at 5 PM"
rsa_cipher = public_key.encrypt(short_msg, oaep)
print("Encrypted with PUBLIC key (hex, first 64):", rsa_cipher.hex()[:64], "...")
print("Decrypted with PRIVATE key:", private_key.decrypt(rsa_cipher, oaep).decode())

# ---------------------------------------------------------------
# 3. HASHING (SHA-256) - one-way, fixed-length fingerprint
# ---------------------------------------------------------------
print("\n[3] HASHING - SHA-256")
h1 = hashlib.sha256(message).hexdigest()
h2 = hashlib.sha256(message + b".").hexdigest()   # change of 1 character
print("Hash of message     :", h1)
print("Hash (1 char added) :", h2)
print("Avalanche effect - hashes completely different:", h1 != h2)

# Password hashing with salt (PBKDF2) - how passwords should be stored
password = b"MyPassword@123"
salt = os.urandom(16)
pw_hash = hashlib.pbkdf2_hmac("sha256", password, salt, 200_000)
print("Salted password hash:", pw_hash.hex())
check = hashlib.pbkdf2_hmac("sha256", b"MyPassword@123", salt, 200_000)
print("Correct password verifies:", check == pw_hash)
wrong = hashlib.pbkdf2_hmac("sha256", b"wrongpass", salt, 200_000)
print("Wrong password verifies  :", wrong == pw_hash)

# ---------------------------------------------------------------
# 4. DIGITAL SIGNATURE (RSA-PSS with SHA-256)
# ---------------------------------------------------------------
print("\n[4] DIGITAL SIGNATURE - RSA-PSS")
pss = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)
signature = private_key.sign(message, pss, hashes.SHA256())   # signed with PRIVATE key
print("Signature (hex, first 64):", signature.hex()[:64], "...")
try:
    public_key.verify(signature, message, pss, hashes.SHA256())  # verified with PUBLIC key
    print("Original message : signature VALID")
except InvalidSignature:
    print("Original message : signature INVALID")
try:
    public_key.verify(signature, b"Marks: 99", pss, hashes.SHA256())
    print("Modified message : signature VALID")
except InvalidSignature:
    print("Modified message : signature INVALID (tampering detected)")

print("\nPractical completed.")
