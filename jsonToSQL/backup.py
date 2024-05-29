import os

def backup_database(output_db):
    backup_dir = 'db_backups'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_suffix = '-bak'
    backup_index = 1
    backup_db = f"{output_db}{backup_suffix}{backup_index}.db"

    while os.path.exists(backup_db):
        backup_index += 1
        backup_db = f"{output_db}{backup_suffix}{backup_index}.db"

    os.rename(output_db, os.path.join(backup_dir, os.path.basename(backup_db)))