import os
from backup import backup_database
from database import initialize_database, insert_data
from json_parser import load_json, process_data, setup_ratedata

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
        rate_data_list = setup_ratedata(rates_data)
        for rate_data in rate_data_list:
            print(rate_data)

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    print(f"updated {output_db}")

if __name__ == '__main__':
    main()