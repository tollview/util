import sqlite3
import json
from models.gate import Gate
from models.dbratematch import DbRateMatch

def initialize_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gates
                      (i INTEGER, name TEXT, code TEXT, cost REAL, plaza_id INTEGER, locx REAL, locy REAL, cardinality TEXT)''')
    return conn, cursor

def insert_data(cursor, gate_list, matched_data, json_file):
    index = 0
    for gate in gate_list:
        cursor.execute("INSERT INTO gates VALUES (?, ?, ?, NULL, NULL, ?, ?, ?)",
                       (index, gate.name, gate.code, gate.locx, gate.locy, gate.cardinality))
        index += 1
    
    for match in matched_data:
        cursor.execute("UPDATE gates SET cost = ?, plaza_id = ? WHERE code = ?", 
                       (match.cost, match.plaza_id, match.code))

    cursor.execute("SELECT * FROM gates")
    all_data = cursor.fetchall()
    save_json_representation(all_data, json_file)

def save_json_representation(data, json_file):
    json_data = []
    for row in data:
        entry = {
            "index": row[0],
            "name": row[1],
            "source_name": row[2],
            "cost": row[3],
            "source_id": row[4],
            "latitude": row[5],
            "longitude": row[6],
            "cardinality": row[7]
        }
        json_data.append(entry)
    
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"JSON data saved to {json_file}")
