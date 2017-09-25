import hashlib


def sha256(plain_text):
    encoder = hashlib.sha256()
    encoder.update(plain_text.encode("utf8"))
    return encoder.hexdigest()
