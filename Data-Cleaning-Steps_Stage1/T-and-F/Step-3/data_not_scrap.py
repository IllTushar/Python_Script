import pandas as pd


def process_data(read_csv_file):
    not_scrap_data = read_csv_file[read_csv_file['Extract'].isna()]
    return not_scrap_data


if __name__ == '__main__':
    read_csv_file = pd.read_csv(r'C:\Users\gtush\Desktop\DrugBank_Set2\Drug_bank_data_2.csv')

    data_frame = process_data(read_csv_file)
    data_frame.to_csv(r'C:\Users\gtush\Desktop\DrugBank_Set2\not_scrap_data.csv', index=False)
