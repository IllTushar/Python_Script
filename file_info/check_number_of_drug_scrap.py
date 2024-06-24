import pandas as pd

if __name__ == '__main__':
    # Read the CSV file
    read_csv = pd.read_csv(r'D:\Laptop5-data\Drug Bank Data_5\Approved_DrugBankData_5.csv')

    # Extract the 'Extract' column
    extract = read_csv['Extract']
    # Count the rows where 'T' is present
    count_T = extract.str.contains('EN', na=False).sum()
    # count_N = extract.str.contains('N', na=False).sum()
    # count_EN = extract.str.contains('EN', na=False).sum()
    total = count_T

    # Print the result
    print("L4-> ", total)
