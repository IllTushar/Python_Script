import pandas as pd


def data_process(read_file_csv):
    # Drop duplicate rows based on 'Dirty_Effect' column
    data_set = read_file_csv.drop_duplicates(subset=['Dirty_Effect'])
    return data_set


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Effects\risk-level_1.csv'
    read_file_csv = pd.read_csv(file_path)

    data = data_process(read_file_csv)
    output = r'C:\Users\gtush\Desktop\Effects\risk-level_2.csv'
    data.to_csv(output, index=False)
