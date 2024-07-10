import pandas as pd


def data_process(read_file):
    for index, row in read_file.iterrows():
        base_url = row['Base_Drug URL']
        drug_url = row['URL']
        base_split = base_url.split("/")
        drug_split = drug_url.split("/")
        read_file.at[index, "BaseDrugCode"] = base_split[-1].strip()
        read_file.at[index, 'DrugCode'] = drug_split[-1].strip()
    return read_file


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv'
    read_file = pd.read_csv(file_path)
    read_file = data_process(read_file)
    read_file.to_csv(file_path, index=False)
