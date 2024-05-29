import sqlite3
from models.dbratematch import DbRateMatch

def initialize_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gates
                      (i INTEGER, name TEXT, code TEXT, cost REAL)''')
    return conn, cursor

def insert_data(cursor, gate_list, matched_data):
    for gate in gate_list:
        cursor.execute("INSERT INTO gates VALUES (?, ?, ?, NULL)",
                       (gate.index, gate.name, gate.code))
    
    for match in matched_data:
        cursor.execute("UPDATE gates SET cost = ? WHERE code = ?", 
                       (match.cost, match.code))