import cv2
import hashlib

def image_fingerprint(image_path):
    """
    Create a SHA256 hash from the image bytes.
    If the image changes even slightly, the fingerprint changes.
    """
    img = cv2.imread(image_path)

    success, encoded = cv2.imencode(".png", img)

    if not success:
        return None

    return hashlib.sha256(encoded.tobytes()).hexdigest()