from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# create the keys
def key_pair():
    private_key=rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key=private_key.public_key()
    return private_key, public_key

# encrypt message
def encrypt(message, public_key):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


# decrypt with private key
def decrypt(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# save the key function
def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# load the key function
def load_key(filename):
    with open(filename, 'rb') as key_file:
        key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
    return key







private_key, public_key = key_pair()

# private key saved
save_key(private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
), 'private_key.pem')

# public key saved
save_key(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
), 'public_key.pem')

# the following are used to load the keys from respective files
# loaded_private_key = load_key('private_key.pem')
# loaded_public_key = load_key('public_key.pem')



message = input("Enter message to encryt: ")
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)
print(f"Encrypted message: {ciphertext}")
#print(f"Decrypted message: {decrypted_message}")
