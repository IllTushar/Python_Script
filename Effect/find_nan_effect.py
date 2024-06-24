import pandas as pd


def find_nan(read_csv):
    none_effect = read_csv[read_csv['Effect'].isna()]
    return none_effect


if __name__ == '__main__':
    for i in range(1, 9):
        read_csv_file = pd.read_csv(
            fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file_part{i}.csv')

        new_csv = find_nan(read_csv_file)
        new_csv.to_csv(fr'C:\Users\gtush\Desktop\FinalCsv\nan_effect_file\effect{i}.csv', index=False)
        print(fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file_part{i}.csv')
