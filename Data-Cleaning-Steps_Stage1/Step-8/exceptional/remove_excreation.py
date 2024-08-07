import pandas as pd


def process_data(read_csv):
    for index, row in read_csv.iterrows():
        if 'excretion' in row['remaining_sentence'] and pd.isna(row['Effect']):
            read_csv.at[index, 'remaining_sentence'] = row['remaining_sentence'].replace('excretion', '').strip()
            read_csv.at[index, 'Effect'] = 'excretion'
    return read_csv


if __name__ == '__main__':
    for i in range(1, 2):
        file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
        read_csv = pd.read_csv(file_path)
        print(file_path)
        read_csv = process_data(read_csv)
        read_csv.to_csv(file_path, index=False)
