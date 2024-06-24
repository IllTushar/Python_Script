import pandas as pd

if __name__ == '__main__':
    read_csv_file = pd.read_csv(
            r'C:\Users\gtush\Desktop\FinalCsv\complete_extract_data_file2.csv')
    read_csv_file = read_csv_file.drop(columns=['Direction'])
    read_csv_file = read_csv_file.drop(columns=['remaining_sentence'])
    read_csv_file.to_csv(
            r'C:\Users\gtush\Desktop\FinalCsv\complete_extract_data_file2.csv',
            index=False)
