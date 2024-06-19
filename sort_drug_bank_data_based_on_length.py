import pandas as pd

if __name__ == '__main__':
    read_drug_bank_file = pd.read_csv(r'C:\Users\gtush\Desktop\DrugBankData\FinalMergeDrugBank.csv')
    # print(read_drug_bank_file.columns)
    print(read_drug_bank_file.shape)
    sort_the_drug_name = sorted(read_drug_bank_file['Name'], key=len, reverse=True)
    data_frame = pd.DataFrame(sort_the_drug_name)
    data_frame.to_csv(r'C:\Users\gtush\Desktop\DrugBankData\sorted_name_dec.csv', index=False,header=['Name'])
