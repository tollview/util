import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

load_dotenv()
service_account_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tollview-dfw-default-rtdb.firebaseio.com/'
})

ref = db.reference('/gates')
data = ref.get()

output_dir='./API/json/'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'dbsnapshot.json')

with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f'Data saved to {output_file}')