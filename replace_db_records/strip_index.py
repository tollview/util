import json

def strip_index_from_gates(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        for gate in data:
            if 'index' in gate:
                del gate['index']

        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"'index' keys removed from gates in {json_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    json_file_path = './dfwGantryList.json'
    strip_index_from_gates(json_file_path)