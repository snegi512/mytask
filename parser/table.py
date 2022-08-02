import array
from terminaltables import SingleTable


#table generator
def print_table(arr:array) -> SingleTable:
    table_data = [['Name','Method','Params']]
    for obj in arr:
        table_data.append([obj['name'],obj['method'],
            generate_str_params(obj['params'])])

    table = SingleTable(table_data)
    table.inner_row_border = True

    print(table.table)


# collects a string of params
def generate_str_params(arr):
    res_str = ''
    for i in arr:
        res_str+=str(i)+'\n'
    return res_str


if __name__ == '__main__':
    table_data = [
        {'name': 'Send transaction (async)', 'method': 'broadcast_tx_async', 'params': ['[SignedTransaction encoded in base64]']}
    ]
    print_table(table_data)