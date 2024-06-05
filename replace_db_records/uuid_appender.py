import json
import uuid

def append_uuid_to_gates(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        for gate in data:
            gate['gateId'] = str(uuid.uuid4())

        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"UUIDs appended to gates in {json_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    json_file_path = './dfwGantryList.json'
    append_uuid_to_gates(json_file_path)
