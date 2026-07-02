import hashlib
import uuid

def create_uuid():
    return str(uuid.uuid4())

def fingerprint(text):
    return hashlib.sha256(text.encode()).hexdigest()