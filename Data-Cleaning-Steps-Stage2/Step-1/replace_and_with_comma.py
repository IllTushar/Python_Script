import pandas as pd


def replace_and_with_comma(read_csv_file):
    for index, row in read_csv_file.iterrows():
        if 'and' in row['Effect']:
            read_csv_file.at[index, 'Effect'] = row['Effect'].replace('and', ',').strip()
        elif ', ,' in row['Effect']:
            read_csv_file.at[index, 'Effect'] = row['Effect'].replace(', ,', ',').strip()

    return read_csv_file


if __name__ == '__main__':
    for i in range(1, 3):
        file_path = fr'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\Complete{i}.csv'
        read_csv_file = pd.read_csv(file_path)
        read_csv_file = replace_and_with_comma(read_csv_file)
        read_csv_file.to_csv(file_path, index=False)
        print(file_path)
