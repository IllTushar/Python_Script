import pandas as pd


def process_data(read_csv_file):
    for index, row in read_csv_file.iterrows():
        effect = row['Effect']
        if 'anti' in effect.lower():  # Check for 'anti' case-insensitively
            read_csv_file.at[index, 'Effect'] = effect.replace('anti', '').replace('Anti', '').strip()
        elif 'CNS stimulation' in effect:
            read_csv_file.at[index, 'Effect'] = effect.replace("CNS stimulation", "CNS Depression").strip()
        elif 'reduced gastrointestinal motility' in effect:
            read_csv_file.at[index, 'Effect'] = effect.replace('reduced', '').strip()
        elif 'reduced intravascular volume' in effect:
            read_csv_file.at[index, 'Effect'] = effect.replace('reduced', '').strip()
    return read_csv_file


if __name__ == '__main__':
    for i in range(1, 15):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        read_csv_file = pd.read_csv(file_path)
        df = process_data(read_csv_file)
        df.to_csv(file_path, index=False)
