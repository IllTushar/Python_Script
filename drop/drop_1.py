import pandas as pd

if __name__ == '__main__':
    read_csv_file = pd.read_csv(
            r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv')
    read_csv_file = read_csv_file.drop(columns=['Effect_1'])
    # read_csv_file = read_csv_file.drop(columns=['remaining_sentence'])
    read_csv_file.to_csv(
            r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv',
            index=False)
