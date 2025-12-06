# rsa_verify.py

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def verify_message(message: str, signature_hex: str, public_key_path="public.pem"):
    signature = bytes.fromhex(signature_hex)

    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

if __name__ == "__main__":
    msg = input("Xabar: ")
    sig = input("Imzo (HEX): ")

    if verify_message(msg, sig):
        print("Natija: ✔️ IMZO TO‘G‘RI")
    else:
        print("Natija: ✘ IMZO NOTO‘G‘RI")