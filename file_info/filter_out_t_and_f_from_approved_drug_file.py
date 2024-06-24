import pandas as pd

if __name__ == '__main__':
    combined_data_frame = pd.DataFrame()  # Initialize an empty DataFrame to store rows with both 'T' and 'N'

    for i in range(1, 7):
        file_path = fr'C:\Users\gtush\Desktop\approved_base_drug_file_process\Approved_DrugBankData_{i}.csv'
        read_csv = pd.read_csv(file_path)

        # Convert 'Extract' column to string and fill NaN with empty strings
        read_csv['Extract'] = read_csv['Extract'].astype(str).fillna('')

        # Initialize an empty DataFrame for this iteration
        iteration_data_frame = pd.DataFrame()

        # Loop through each row and check if 'Extract' contains both 'T' and 'N'
        for index, row in read_csv.iterrows():
            extract_value = row['Extract']
            if extract_value and 'T' in extract_value or 'N' in extract_value and 'EN' not in extract_value:
                # Append the row to the iteration DataFrame
                iteration_data_frame = pd.concat([iteration_data_frame, pd.DataFrame([row])])

        # Append the filtered rows from this iteration to the combined DataFrame
        combined_data_frame = pd.concat([combined_data_frame, iteration_data_frame])

    # Save the combined DataFrame to a new CSV file
    combined_data_frame.to_csv(
        r'C:\Users\gtush\Desktop\approved_base_drug_file_process\Filtered_Approved_DrugBankData_T_and_N.csv',
        index=False)
