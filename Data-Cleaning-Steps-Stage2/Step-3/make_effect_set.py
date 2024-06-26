import pandas as pd


def process_csv_file(read_csv_file):
    data_set = set()
    for index, row in read_csv_file.iterrows():
        effect = row['Effect'].strip()
        if ',' in effect:
            splits = effect.split(',')
            for data in splits:
                data_set.add(data.strip())
        else:
            data_set.add(effect)

    return data_set


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv'
    read_csv_file = pd.read_csv(file_path)

    data = process_csv_file(read_csv_file)
    df = pd.DataFrame({"Effects": list(data)})
    # print(df)
    output_path = r'C:\Users\gtush\Desktop\Effects\effect_data.csv'
    df.to_csv(output_path, index=False)
    print(output_path)
