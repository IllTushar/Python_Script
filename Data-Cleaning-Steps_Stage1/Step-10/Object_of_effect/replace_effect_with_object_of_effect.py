import pandas as pd


def process_object_of_effect(read_file_csv):
    # Update 'Effect' with 'object_of_effect' values where they are not NaN
    read_file_csv['Effect'] = read_file_csv['object_of_effect'].combine_first(read_file_csv['Effect'])
    return read_file_csv


if __name__ == '__main__':
    for i in range(1, 2):
        try:
            file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
            read_file_csv = pd.read_csv(file_path)

            read_file_csv = process_object_of_effect(read_file_csv)

            read_file_csv.to_csv(file_path, index=False)
            print(f'Processed: {file_path}')
        except Exception as e:
            print(f'Error processing {file_path}: {e}')
