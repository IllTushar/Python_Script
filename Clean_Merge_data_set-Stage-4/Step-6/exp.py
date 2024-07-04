import pandas as pd


def process_data(merge_file):
    for index, row in merge_file.iterrows():
        effect = row['Effect']
        if 'qtc prolongation' in effect:
            merge_file.at[index, 'severity level_1'] = 5
        elif 'qtc-prolonging activities' in effect:
            merge_file.at[index, 'severity level_1'] = 5
        elif 'central nervous system depressant (cns depressant) activities' in effect:
            merge_file.at[index, 'severity level_1'] = 3
        elif 'cns depression' in effect:
            merge_file.at[index, 'severity level_1'] = 3
        elif 'thrombosis' in effect:
            merge_file.at[index, 'severity level_1'] = 5
    return merge_file


if __name__ == '__main__':
    for i in range(1, 12):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        read_merge_file_path = file_path
        merge_file = pd.read_csv(read_merge_file_path)
        merge_file = process_data(merge_file)

        merge_file.to_csv(read_merge_file_path, index=False)
        print(file_path)
