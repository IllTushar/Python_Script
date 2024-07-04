import pandas as pd


def data_process(read_file_csv_effect, read_file_csv_complete_data):
    # Create a list of Cleaned_Effect values
    cleaned_effects = read_file_csv_effect['Clean_Effect'].tolist()

    # Use a lambda function to check if any Cleaned_Effect is in the Effect column
    result = read_file_csv_complete_data[
        read_file_csv_complete_data['Effect'].apply(lambda x: any(effect in x for effect in cleaned_effects))]

    return result


if __name__ == '__main__':
    file_path_for_effect_data = r'C:\Users\gtush\Desktop\Effects\risk_level\risk-level_none.csv'
    read_file_csv_effect = pd.read_csv(file_path_for_effect_data)

    file_path_complete_data = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv'
    read_file_csv_complete_data = pd.read_csv(file_path_complete_data)

    result_data = data_process(read_file_csv_effect, read_file_csv_complete_data)
    df = pd.DataFrame(result_data)
    df.to_csv(r'C:\Users\gtush\Desktop\Effects\risk_level\not_define.csv', index=False)
    # Optionally, save the result to a new CSV file
    # result_data.to_csv(r'C:\Users\gtush\Desktop\result_data.csv', index=False)
