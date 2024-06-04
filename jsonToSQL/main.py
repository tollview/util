import os
from functions.backup import backup_database
from functions.database import initialize_database, insert_data
from functions.json_parser import load_json, process_data, setup_ratedata, setup_locdata
from functions.matcher import match_gates_and_rates, check_cardinality, pair_nswe_codes, log_unmatched_data, match_rates_and_loc

def main():
    dbsnapshot_file = './json/dbsnapshot.json'
    rates_file = './json/RatesResponse.json'
    location_file = './json/LocationsResponse.json'
    output_db = '../gateslist.db'

    if os.path.exists(output_db):
        backup_database(output_db)

    try:
        conn, cursor = initialize_database(output_db)
        db_data = load_json(dbsnapshot_file)
        gate_list = process_data(db_data)
        
        gate_list = check_cardinality(gate_list)
        gate_list = pair_nswe_codes(gate_list)

        rates_data = load_json(rates_file)
        rate_data_list = setup_ratedata(rates_data)

        loc_data = load_json(location_file)
        loc_data_list = setup_locdata(loc_data)

        rate_data_list = match_rates_and_loc(rate_data_list, loc_data_list)
        matched_data, unmatched_data = match_gates_and_rates(gate_list, rate_data_list)

        if unmatched_data:
            log_unmatched_data(unmatched_data)

        insert_data(cursor, gate_list, matched_data)

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    print(f"Updated {output_db}")

if __name__ == '__main__':
    main()
