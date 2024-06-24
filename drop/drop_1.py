import pandas as pd

if __name__ == '__main__':
    for i in range(1, 9):
        read_csv_file = pd.read_csv(
            fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file_part{i}.csv')
        print(fr'C:\Users\gtush\Desktop\sample_output\separation_{i}.csv')
        read_csv_file = read_csv_file.drop(columns=['sentence_without_base_drug'])
        read_csv_file.to_csv(
            fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file_part{i}.csv',
            index=False)
