import sqlite3
from models.gate import Gate
from models.dbratematch import DbRateMatch

def initialize_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gates
                      (i INTEGER, name TEXT, code TEXT, cost REAL, plaza_id INTEGER, locx REAL, locy REAL)''')
    return conn, cursor

def insert_data(cursor, gate_list, matched_data):
    for gate in gate_list:
        cursor.execute("INSERT INTO gates VALUES (?, ?, ?, NULL, NULL, ?, ?)",
                       (gate.index, gate.name, gate.code, gate.locx, gate.locy))
    
    # Update the cost and plaza_id for matched gates
    for match in matched_data:
        cursor.execute("UPDATE gates SET cost = ?, plaza_id = ? WHERE code = ?", 
                       (match.cost, match.plaza_id, match.code))