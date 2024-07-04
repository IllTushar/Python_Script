import pandas as pd

if __name__ == '__main__':
    for i in range(1, 12):
        file_path = fr"C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv"
        read_file_path = pd.read_csv(file_path)
        effect = read_file_path['Effect']
        data = list(map(str.lower, effect))
        read_file_path['Effect'] = data
        read_file_path.to_csv(file_path, index=False)
