import os
from backup import backup_database
from database import initialize_database, insert_data
from json_parser import load_json, process_data

def main():
    dbsnapshot_file = './json/dbsnapshot.json'
    rates_file = './json/RatesResponse.json'
    location_file = './json/LocationResponse.json'
    output_db = '../gateslist.db'

    if os.path.exists(output_db):
        backup_database(output_db)

    try:
        conn, cursor = initialize_database(output_db)
        db_data = load_json(dbsnapshot_file)
        gate_list = process_data(db_data)
        insert_data(cursor, gate_list)

        rates_data = load_json(rates_file)

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"Database updated: {output_db}")
        conn.close()
    finally:
        if 'conn' in locals() and hasattr(conn, 'close'):
            conn.close()

if __name__ == '__main__':
    main()
