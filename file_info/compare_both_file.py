import pandas as pd

if __name__ == '__main__':
    # Read the CSV files
    read_csv_1 = pd.read_csv(
        r'C:\Users\gtush\Desktop\approved_base_drug_file_process\Approved_Data_with_T_and_F\DrugBankData.csv')

    read_csv_2 = pd.read_csv(
        r'C:\Users\gtush\Desktop\approved_base_drug_file_process\Approved_Data_with_T_and_F\Filtered_Approved_DrugBankData_T_and_N.csv')

    # Get the 'Name' columns and convert to sets
    name_2 = set(read_csv_2['Name'])

    # Filter read_csv_1 to get rows where 'Name' is not in read_csv_2
    df_not_found = read_csv_1[~read_csv_1['Name'].isin(name_2)]

    # Save the DataFrame to a CSV file
    df_not_found.to_csv(r'C:\Users\gtush\Desktop\approved_base_drug_file_process\Approved_Data_with_T_and_F\drug_not_scrap.csv', index=False)
