# run_scraper.py at startup, the names, methods and parameters are parsed on the RPC Endpoints | NEAR Documentation page. 
# The script accepts the command-line startup argument “--dry_run".
# If dry_run is True, the script should print the result as a table to the console.
# Otherwise, the script should create new records in the collected_data table in the database. 
# If the table is not empty, first all existing records should be deleted from the table, and then new ones should be added.

import argparse
from parser import get_data
from table import print_table
from db_put import put_data

def create_parser ():
    parser = argparse.ArgumentParser(description='Parsing of names, methods and parameters on the RPC Endpoints | NEAR Documentation page')
    parser.add_argument('--dry_run', type=str, default='true',
                    help='true - result is in the form of a table in the console\nfalse -  result to the database\n(default: true)')
    return parser


if __name__ == '__main__':
    input_par = create_parser()
    namespace = input_par.parse_args()
    mode:str = str.lower(namespace.dry_run)
    d = get_data()
    if(mode == 'true'):
        print_table(d)
    if (mode == 'false'):
        put_data(d)
    # print(d)