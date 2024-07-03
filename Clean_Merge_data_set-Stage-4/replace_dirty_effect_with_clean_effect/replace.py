import pandas as pd


def data_process(read_file_csv):
    # Update 'Dirty_Effect' where 'Clean_Effect' is not NaN
    mask = ~read_file_csv['Clean_Name'].isna()
    read_file_csv.loc[mask, 'Dirty_Effect'] = read_file_csv['Clean_Name']
    return read_file_csv


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Effects\risk-level.csv'
    read_file_csv = pd.read_csv(file_path)
    # print(read_file_csv.columns)
    df = data_process(read_file_csv)
    output_file = r'C:\Users\gtush\Desktop\Effects\risk-level_1.csv'
    df.to_csv(output_file, index=False)
