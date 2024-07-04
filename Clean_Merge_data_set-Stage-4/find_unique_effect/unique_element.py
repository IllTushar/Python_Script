import pandas as pd


def not_present(server_level):
    if '1' in server_level or '2' in server_level or '3' in server_level or '4' in server_level or '5' in server_level:
        return False
    else:
        return True


def process_data(read_file):
    server_level = str(read_file['severity level_1'])
    data = list(filter(not_present, server_level))
    print('list', data)
    data_set = {i for i in data}
    print('set', data_set)


if __name__ == '__main__':
    read_file = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\MergeFile2.csv')
    # print(read_file.columns)
    process_data(read_file)
