import pandas as pd


def process_data(merge_file, effect_code):
    # Create a dictionary for effect codes
    effect_codes = effect_code.set_index('Cleaned_Effect')['Code'].to_dict()

    # List of effect columns to be processed
    effect_columns = ['Effect_1', 'Effect_2', 'Effect_3', 'Effect_4', 'Effect_5']

    # Replace effect codes using the dictionary
    merge_file[effect_columns] = merge_file[effect_columns].applymap(lambda x: effect_codes.get(x, x))

    return merge_file


if __name__ == '__main__':
    read_merge_file_path = r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv'
    merge_file = pd.read_csv(read_merge_file_path)

    effect_code_file_path = r'C:\Users\gtush\Desktop\data_cleaning\Effects_Cleaner_With_Code.csv'
    effect_code = pd.read_csv(effect_code_file_path)

    merge_file = process_data(merge_file, effect_code)

    merge_file.to_csv(read_merge_file_path, index=False)
