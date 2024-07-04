import pandas as pd


def data_process(read_file_csv):
    # Drop duplicate rows based on 'Dirty_Effect' column
    data_set = read_file_csv.drop_duplicates(subset=['Dirty_Effect'])
    return data_set


def all_small(file):
    for index, row in file.iterrows():
        file.at[index, 'Clean_Effect'] = row['Clean_Effect'].lower()
    return file


if __name__ == '__main__':
    # file_path = r'C:\Users\gtush\Desktop\Effects\risk-level_1.csv'
    # read_file_csv = pd.read_csv(file_path)

    # data = data_process(read_file_csv)
    output = r'C:\Users\gtush\Desktop\Effects\risk_level\risk-level_none.csv'
    file = pd.read_csv(output)
    data = all_small(file)
    data.to_csv(output, index=False)
