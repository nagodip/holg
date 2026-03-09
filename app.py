import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/config', methods=['GET'])
def get_config():
    # Ab ye keys direct code mein nahi hain, Render dashboard se aayengi
    config_data = {
        "firebase": {
            "apiKey": os.environ.get("FIREBASE_API_KEY"),
            "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
            "databaseURL": os.environ.get("FIREBASE_DATABASE_URL"),
            "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
            "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
            "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID"),
            "appId": os.environ.get("FIREBASE_APP_ID"),
            "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID")
        },
        "cloudinary": {
            "cloudName": os.environ.get("CLOUDINARY_CLOUD_NAME"),
            "uploadPreset": os.environ.get("CLOUDINARY_UPLOAD_PRESET")
        }
    }
    return jsonify(config_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)