import pandas as pd


def process_data(read_csv):
    data_set = []
    for index, row in read_csv.iterrows():
        if 'N' in str(row['Extract']):
            data_set.append(row)
    return pd.DataFrame(data_set)


def process_data_entries(read_csv):
    data_set = read_csv[~read_csv['Entries'].isna()]
    return data_set


if __name__ == '__main__':
    read_csv = pd.read_csv(r'C:\Users\gtush\Desktop\DrugBankScraping\DataSetPresent_N_2.csv')
    # df = process_data(read_csv)
    df = process_data_entries(read_csv)
    df.to_csv(r'C:\Users\gtush\Desktop\DrugBankScraping\DataSetPresent_Only_entries.csv', index=False)
