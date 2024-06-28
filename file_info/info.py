import pandas as pd

if __name__ == '__main__':
    read_file = pd.read_csv(
        r'C:\Users\gtush\Desktop\Collection_2\DB01193.csv')
    #
    # read_file_2 = pd.read_csv(
    #     r'C:\Users\gtush\Desktop\FinalCsv\complete_extract_data_file2.csv')
    print(read_file.shape)
    # print(read_file_2.shape)
