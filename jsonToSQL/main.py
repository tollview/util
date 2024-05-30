import os
from functions.backup import backup_database
from functions.database import initialize_database, insert_data
from functions.json_parser import load_json, process_data, setup_ratedata
from functions.matcher import match_gates_and_rates

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
        rates_data = load_json(rates_file)
        rate_data_list = setup_ratedata(rates_data)

        matched_data = match_gates_and_rates(gate_list, rate_data_list)
        insert_data(cursor, gate_list, matched_data)

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    print(f"updated {output_db}")

if __name__ == '__main__':
    main()