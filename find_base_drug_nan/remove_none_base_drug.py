import pandas as pd


def fill_all_base_drug_none(df):
    # Check for None (or NaN) values in the 'Base_drug' column
    none_base_drug = df[df['Base_drug'].isna()]
    return none_base_drug


if __name__ == '__main__':
    for i in range(1, 541):
        # Read the CSV file into a DataFrame
        read_csv = pd.read_csv(fr'C:\Users\gtush\Desktop\sample_output\separation_{i}.csv')
        # print(read_csv.columns)

        # Get rows where 'Base_drug' is None
        none_base_drug_df = fill_all_base_drug_none(read_csv)

        # Save the new DataFrame to a new CSV file
        none_base_drug_df.to_csv(fr'C:\Users\gtush\Desktop\NoneCsv\none_base_drug{i}.csv', index=False)
        print(fr"C:\Users\gtush\Desktop\NoneCsv\none_base_drug{i}.csv")
