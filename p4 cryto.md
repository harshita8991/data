
# Practical 4: Cryptography

## Aim
To learn different cryptographic techniques and tools, such as encryption, hashing and digital signatures, and implement them in practice.

## Requirements
- Python 3.8 or above
- `cryptography` library: `pip install cryptography`

## Techniques Implemented

| Technique | Algorithm Used | Purpose |
|---|---|---|
| Symmetric Encryption | AES-256-GCM | Keeps data confidential using one shared key, and detects tampering |
| Asymmetric Encryption | RSA-2048 with OAEP | Encrypts with a public key, decrypts with a private key |
| Hashing | SHA-256 | Creates a fixed-length one-way fingerprint to check integrity |
| Password Hashing | PBKDF2-HMAC-SHA256 with salt | Stores passwords safely so they are hard to crack |
| Digital Signature | RSA-PSS with SHA-256 | Proves who sent a message and that it was not changed |

## Procedure
1. Install the library: `pip install cryptography`
2. Save the program as `crypto_practical.py`
3. Run it: `python crypto_practical.py`
4. Observe the output of each technique.

## Sample Output
(Ciphertexts, signatures and salted hashes change on every run because keys, nonces and salts are random. The SHA-256 hashes stay the same for the same input.)

```
============================================================
ORIGINAL MESSAGE: Student ID: 12345 | Marks: 92 | Confidential
============================================================

[1] SYMMETRIC ENCRYPTION - AES-256-GCM
Ciphertext (hex): 60fc2f7a5beb213d9f07fffb0aa30ccd...
Decrypted       : Student ID: 12345 | Marks: 92 | Confidential
Tampered ciphertext rejected (integrity check works)

[2] ASYMMETRIC ENCRYPTION - RSA-2048
Encrypted with PUBLIC key (hex, first 64): 2d0d8d55fef2d7707b7fc3bc420a8c29... ...
Decrypted with PRIVATE key: Secret: meet at 5 PM

[3] HASHING - SHA-256
Hash of message     : 864147ef107310959d1efa373fea639342cfb1875392ab88af505a1ae8286266
Hash (1 char added) : 404c4067988fe77638adaa72ed71b5986022c61004ab0932a1a82dedbdfe7802
Avalanche effect - hashes completely different: True
Salted password hash: 074b53cb0159a7a5b155720ee2469c56dd7cc5580dead56536c3ba1854800c03
Correct password verifies: True
Wrong password verifies  : False

[4] DIGITAL SIGNATURE - RSA-PSS
Signature (hex, first 64): 38d8b6ed9666cd97143945d457449718... ...
Original message : signature VALID
Modified message : signature INVALID (tampering detected)

Practical completed.
```

## Observations
- AES-256-GCM encrypts the data quickly, and changing even one byte of the ciphertext makes decryption fail, so it also protects integrity.
- RSA uses two keys: anyone can encrypt with the public key, but only the private key holder can decrypt. It is slower and only suitable for small data, so in practice it is used to share the AES key.
- SHA-256 always gives a 64-character hex output. Adding one character changes the whole hash (avalanche effect), and the hash cannot be reversed.
- Salting makes sure two users with the same password get different stored hashes, and the many PBKDF2 iterations slow down brute-force attacks.
- A digital signature is created with the private key and checked with the public key. Any change to the message makes verification fail, which gives integrity, authentication and non-repudiation.

## Relevance to Data Privacy
- **Encryption** protects personal data at rest and in transit (confidentiality).
- **Hashing** protects stored passwords and verifies that data has not been altered (integrity).
- **Digital signatures** confirm the identity of the sender and prevent denial of authorship (authenticity).
- These techniques support the "security safeguards" required by laws such as the DPDP Act 2023 and GDPR.

## Result
Encryption, hashing and digital signatures were successfully implemented and tested in Python.

## Conclusion
Cryptographic techniques are essential for protecting personal data. Symmetric encryption secures data efficiently, asymmetric cryptography allows safe key exchange and signing, and hashing protects passwords and verifies integrity. Used together, they provide confidentiality, integrity and authentication.
