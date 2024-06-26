import pandas as pd


def process_the_serum_concentration(row):
    if 'higher serum level' in row['Effect']:
        row.at['Effect'] = 'serum concentration'
        row.at['Direction'] = 'increased'
    elif 'lower serum level' in row['Effect']:
        row.at['Effect'] = 'serum concentration'
        row.at['Direction'] = 'decreased'
    elif 'absorption' in row['Effect']:
        row.at['Effect'] = 'serum concentration'
    else:
        pass
    return row


if __name__ == '__main__':
    for i in range(1, 9):
        file_path = fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file2_part{i}.csv'

        read_file_csv = pd.read_csv(file_path)

        read_file_csv = read_file_csv.apply(process_the_serum_concentration, axis=1)

        read_file_csv.to_csv(file_path, index=False)
        print('file path', file_path)
