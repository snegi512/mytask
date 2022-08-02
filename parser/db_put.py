
import array

from os.path import abspath, split
import sys
dir = split(split(abspath(__file__))[0])[0]
sys.path.append(dir)
import db




def generate_str_params(arr):
    res_str = ''
    for i in arr:
        res_str+=str(i)+'\n'
    return res_str


def put_data(arr:array):
    db_data = db.get_db_data()
    conn = db_data['conn']
    collected_data = db_data['collected_data']
    delete_query = collected_data.delete() # DELETE data
    conn.execute(delete_query)
    for obj in arr:
        ins_collected_data = collected_data.insert().values(title = obj['name'], method_name = obj['method'], params = generate_str_params(obj['params']))
        conn.execute(ins_collected_data)

