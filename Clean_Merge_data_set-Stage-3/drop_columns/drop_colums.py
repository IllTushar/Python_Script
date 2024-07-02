import pandas as pd

if __name__ == '__main__':
    for i in range(1, 15):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        read_file_csv = pd.read_csv(file_path)
        drop_column = ['Effect_1', 'Effect_2', 'Effect_3', 'Effect_4', 'Effect_5']
        read_file_csv = read_file_csv.drop(columns=drop_column)
        read_file_csv.to_csv(file_path, index=False)
        print(file_path)

