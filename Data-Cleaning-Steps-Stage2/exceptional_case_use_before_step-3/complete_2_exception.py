import pandas as pd


def handle_exception(read_csv):
    for index, row in read_csv.iterrows():
        if 'an active metabolite of ,' in row['Effect']:
            read_csv.at[index, 'Effect'] = 'serum concentration ' + row['Effect']
    return read_csv


def handle_exception_2(read_csv):
    for index, row in read_csv.iterrows():
        if 'an active metabolite of' in row['Effect']:
            splits = row['Effect'].split(",")
            sentence = '-'.join([split.strip() for split in splits])
            read_csv.at[index, 'Effect'] = sentence
    return read_csv


if __name__ == '__main__':
    # for i in range(1, 3):
    file_path = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\MergeFile2.csv'
    read_csv = pd.read_csv(file_path)

    # read_csv = handle_exception(read_csv)
    read_csv = handle_exception_2(read_csv)

    read_csv.to_csv(file_path, index=False)
