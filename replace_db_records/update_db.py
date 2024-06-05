import os
import json
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db

def upload_json_to_firebase(json_file, service_account_key, database_url, firebase_path):
    if not firebase_admin._apps:
        cred = credentials.Certificate(service_account_key)
        firebase_admin.initialize_app(cred, {'databaseURL': database_url})

    with open(json_file, 'r') as f:
        data = json.load(f)

    ref = db.reference(firebase_path)
    ref.set(data)

def main():
    load_dotenv()

    service_account_key = os.getenv('FIREBASE_CREDENTIALS_PATH')
    database_url = 'https://tollview-dfw-default-rtdb.firebaseio.com'
    firebase_path = 'gates/'
    current_json = './dfwGantryList.json'

    if not service_account_key:
        raise ValueError("FIREBASE_CREDENTIALS_PATH is not set in the environment variables or .env file")

    upload_json_to_firebase(current_json, service_account_key, database_url, firebase_path)

if __name__ == '__main__':
    main()
