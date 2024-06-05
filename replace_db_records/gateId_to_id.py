import json

def rename_gateId_to_id(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        for gate in data:
            if 'gateId' in gate:
                gate['id'] = gate.pop('gateId')

        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"'gateId' keys renamed to 'id' in {json_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    json_file_path = './dfwGantryList.json'
    rename_gateId_to_id(json_file_path)
