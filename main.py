from app import app
import os

UPLOAD_FOLDER = "upload"

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(port=3000, debug=True)
