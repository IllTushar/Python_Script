import pandas as pd

if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv'
    read_file_csv = pd.read_csv(file_path)
    drop_column = ['Effect_1', 'Effect_2', 'Effect_3', 'Effect_4', 'Effect_5']
    read_file_csv = read_file_csv.drop(columns=drop_column)
    read_file_csv.to_csv(file_path, index=False)
