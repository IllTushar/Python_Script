import pandas as pd

if __name__ == '__main__':
    for i in range(1, 12):
        file_path = fr"C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv"
        read_file_path = pd.read_csv(file_path)
        col = ['severity level_1', 'severity level_2', 'severity level_3', 'severity level_4', 'severity level_5']
        read_file_path = read_file_path.drop(columns=col)
        read_file_path.to_csv(file_path, index=False)
        print(file_path)
