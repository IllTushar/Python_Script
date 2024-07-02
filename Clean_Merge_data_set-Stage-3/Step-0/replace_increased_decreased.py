import pandas as pd


def replace_increase_decreased(read_csv):
    for idx, row in read_csv.iterrows():
        direction = row['Direction']
        if 'increased' in direction:
            read_csv.at[idx, 'Direction'] = direction.replace('increased', '+')
        elif 'decreased' in direction:
            read_csv.at[idx, 'Direction'] = direction.replace("decreased", '-')
    return read_csv


if __name__ == '__main__':
    for i in range(1, 15):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        read_csv = pd.read_csv(file_path)
        print(file_path)
        df = replace_increase_decreased(read_csv)
        df.to_csv(file_path, index=False)
