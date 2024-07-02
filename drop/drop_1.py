import pandas as pd

if __name__ == '__main__':
    read_csv_file = pd.read_csv(
        r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_merge_file_1.csv')
    drop_col = ['Effect_1', 'Effect_2', 'Effect_3', 'Effect_3', 'Effect_4', 'Effect_5']
    read_csv_file = read_csv_file.drop(columns=drop_col)
    # read_csv_file = read_csv_file.drop(columns=['remaining_sentence'])
    read_csv_file.to_csv(
        r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_merge_file_1.csv',
        index=False)
