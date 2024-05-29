from database import initialize_database, insert_data
from json_parser import load_json, process_data

def main():
    input_file = './json/dbsnapshot.json'
    output_db = '../gateslist.db'

    conn, cursor = initialize_database(output_db)
    data = load_json(input_file)
    gate_list = process_data(data)
    insert_data(cursor, gate_list)
    conn.commit()
    conn.close()
    print(f"updated {output_db}")

if __name__ == '__main__':
    main()