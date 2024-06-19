import pandas as pd


def merge_data_set(i, file_list):
    # Read the CSV files
    file_path = fr'C:\Users\gtush\Desktop\NoneCsv\none_base_drug{i}.csv'
    read_file = pd.read_csv(file_path)
    file_list.append(read_file)
    return file_list


if __name__ == '__main__':
    data = []
    for i in range(1, 42):
        data = merge_data_set(i, data)

    concat_file = pd.concat(data, ignore_index=True)

    # Save the result to a new CSV file
    concat_file.to_csv(r'C:\Users\gtush\Desktop\NoneCsv\EmptyBase_drug.csv', index=False)
