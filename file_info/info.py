import pandas as pd

if __name__ == '__main__':
    read_file = pd.read_csv(
        r'C:\Users\gtush\Desktop\FinalCsv\complete_extract_data_file.csv')

    # read_file_2 = pd.read_csv(
    #     r'C:\Users\gtush\Desktop\approved_base_drug_file_process\Approved_Data_with_T_and_F\drug_not_scrap.csv')
    print(read_file.shape)
    # print(read_file_2.shape)
