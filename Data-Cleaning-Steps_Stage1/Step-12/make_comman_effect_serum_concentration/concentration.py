import pandas as pd


def process_the_serum_concentration(row):
    effect_value = str(row['Effect'])
    if 'higher serum level' in effect_value:
        row.at['Effect'] = 'serum concentration'
        row.at['Direction'] = 'increased'
    elif 'lower serum level' in effect_value:
        row.at['Effect'] = 'serum concentration'
        row.at['Direction'] = 'decreased'
    elif 'absorption' in effect_value:
        row.at['Effect'] = 'serum concentration'
    else:
        pass
    return row


if __name__ == '__main__':
    for i in range(1, 2):
        file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'

        read_file_csv = pd.read_csv(file_path)

        read_file_csv = read_file_csv.apply(process_the_serum_concentration, axis=1)

        read_file_csv.to_csv(file_path, index=False)
        print('file path', file_path)
