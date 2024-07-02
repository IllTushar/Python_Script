import pandas as pd


def process_data(read_file_csv):
    read_file_csv = read_file_csv[read_file_csv['Effect_1'].isna()]
    return read_file_csv


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\MergeFile2.csv'
    read_file_csv = pd.read_csv(file_path)
    df = process_data(read_file_csv)
    output_file_path = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\none_effect_1.csv'
    df.to_csv(output_file_path, index=False)
