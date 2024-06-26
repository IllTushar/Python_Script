import pandas as pd


def process_data(read_csv_file):
    scrap_data = read_csv_file[~read_csv_file['Extract'].isna()]
    return scrap_data


if __name__ == '__main__':
    read_csv_file = pd.read_csv(r'C:\Users\gtush\Desktop\DrugBank_Set2\Drug_bank_data_2.csv')

    data_frame = process_data(read_csv_file)
    data_frame.to_csv(r'C:\Users\gtush\Desktop\DrugBank_Set2\TandF\tandf.csv', index=False)
