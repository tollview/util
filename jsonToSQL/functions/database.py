import sqlite3
from models.gate import Gate
from models.dbratematch import DbRateMatch

def initialize_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gates
                      (i INTEGER, name TEXT, code TEXT, cost REAL, plaza_id INTEGER, locx REAL, locy REAL, cardinality TEXT)''')
    return conn, cursor

def insert_data(cursor, gate_list, matched_data):
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