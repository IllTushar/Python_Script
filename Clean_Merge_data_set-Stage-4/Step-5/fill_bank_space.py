import pandas as pd


def data_process(df):
    data = df[df['severity level_1'].isna()]['Effect'].tolist()
    data_set = set()
    for row in data:
        data_set.add(row)
    return list(data_set)


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\MergeFile2.csv'
    read_file_csv = pd.read_csv(file_path)
    data = data_process(read_file_csv)
    df = pd.DataFrame({"Blank_effect": data})
    df.to_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\blank_sever_level.csv',index=False)
