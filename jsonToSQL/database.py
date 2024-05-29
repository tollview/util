import sqlite3

def initialize_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gates
                      (i INTEGER, name TEXT, code TEXT)''')
    return conn, cursor

def insert_data(cursor, gate_list):
    for gate in gate_list:
        cursor.execute("INSERT INTO gates VALUES (?, ?, ?)", 
                       (gate.index, gate.name, gate.code))