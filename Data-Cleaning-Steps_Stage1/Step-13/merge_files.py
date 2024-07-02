import os
import pandas as pd
if __name__ == '__main__':
    # Define the folder containing the CSV files
    folder_path = r'C:\Users\gtush\Desktop\Collection-4'

    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Initialize an empty list to hold the dataframes
    dataframes = []

    # Loop through the list of CSV files and read each one into a dataframe
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        dataframes.append(df)

    # Concatenate all dataframes into one
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged dataframe to a new CSV file
    merged_df.to_csv(r'C:\Users\gtush\Desktop\drug_cleaning\final_merge_unprocess_csv.csv', index=False)

    print("CSV files have been merged successfully into 'merged_output.csv'")

