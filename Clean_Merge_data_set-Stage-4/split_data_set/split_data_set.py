import pandas as pd


def data_process(read_file_csv):
    read_file_csv = read_file_csv[~read_file_csv['Undifined_Code'].isna()]
    return read_file_csv


if __name__ == '__main__':
    read_file_csv = pd.read_csv(r'C:\Users\gtush\Desktop\Effects\risk-level_2.csv')
    data = data_process(read_file_csv)
    data.to_csv(r'C:\Users\gtush\Desktop\Effects\risk-level_none.csv',index=False)
