import json
import sqlite3

class Gate:
    def __init__(self, index, name, code):
        self.index = index
        self.name = name
        self.code = code

input_file = './json/dbsnapshot.json'
output_db = './gateslist.db'

conn = sqlite3.connect(output_db)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE gates
                  (gate_index INTEGER, name TEXT, code TEXT)''')

with open(input_file, 'r') as file:
    data = json.load(file)

gate_list = []

for entry in data:
    index = entry['index']
    name = entry['name']
    code = entry.get('sourceName', entry.get('sourceName ', '!NULL!'))
    gate_list.append(Gate(index, name, code))

for gate in gate_list:
    cursor.execute("INSERT INTO gates VALUES (?, ?, ?)", (gate.index, gate.name, gate.code))

conn.commit()
conn.close()

print(f"updated {output_db}")
