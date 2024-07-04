import pandas as pd


def process_data(merge_file, effect_code):
    # Create a dictionary for effect codes
    effect_codes = effect_code.set_index('Dirty_Effect')['Classification_Code'].to_dict()

    # List of effect columns to be processed
    effect_columns = ['severity level_1', 'severity level_2', 'severity level_3', 'severity level_4',
                      'severity level_5']

    # Replace effect codes using the dictionary
    for column in effect_columns:
        merge_file[column] = merge_file[column].replace(effect_codes)

    return merge_file


if __name__ == '__main__':
    effect_code_file_path = r'C:\Users\gtush\Desktop\Effects\risk_level\risk-level.csv'
    effect_code = pd.read_csv(effect_code_file_path)
    for i in range(1, 12):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        read_merge_file_path = file_path
        merge_file = pd.read_csv(read_merge_file_path)

        merge_file = process_data(merge_file, effect_code)

        merge_file.to_csv(read_merge_file_path, index=False)
        print(file_path)
