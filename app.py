from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# CORS enable karna zaroori hai taki tumhara frontend is API ko call kar sake
CORS(app)

@app.route('/api/config', methods=['GET'])
def get_config():
    # Render Dashboard mein in variables ko Environment Variables (ENV) mein set karna
    config_data = {
        "firebase": {
            "apiKey": os.environ.get("FIREBASE_API_KEY", "AIzaSyAMPzranCB03Wtjn1qoqvS9R2upUxlZ5cw"),
            "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN", "wessit-4766b.firebaseapp.com"),
            "databaseURL": os.environ.get("FIREBASE_DATABASE_URL", "https://wessit-4766b-default-rtdb.firebaseio.com"),
            "projectId": os.environ.get("FIREBASE_PROJECT_ID", "wessit-4766b"),
            "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET", "wessit-4766b.firebasestorage.app"),
            "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID", "430793172456"),
            "appId": os.environ.get("FIREBASE_APP_ID", "1:430793172456:web:5fa38a17446a403423b05d"),
            "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID", "G-WESX7BB5SM")
        },
        "cloudinary": {
            "cloudName": os.environ.get("CLOUDINARY_CLOUD_NAME", "djost0kzi"),
            "uploadPreset": os.environ.get("CLOUDINARY_UPLOAD_PRESET", "nagodipgo")
        }
    }
    return jsonify(config_data)

if __name__ == '__main__':
    # Render ke liye port configuration
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)