# rsa_sign.py

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def sign_message(message: str, private_key_path="private.pem"):
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return signature.hex()

if __name__ == "__main__":
    msg = input("Xabar: ")
    sig = sign_message(msg)
    print("Imzo (HEX):")
    print(sig)