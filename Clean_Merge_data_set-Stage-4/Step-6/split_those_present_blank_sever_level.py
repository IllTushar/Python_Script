import pandas as pd


def data_process(read_blank_file, read_risk_file):
    result_list = []

    for idx, row1 in read_risk_file.iterrows():
        dirty_effect = row1['Dirty_Effect']
        for row2 in read_blank_file['Blank_effect']:
            if dirty_effect in row2:  # Assumes row2 is a string and dirty_effect should be found within it
                result_list.append(tuple(row1))  # Convert Series to tuple for uniqueness

    unique_set = set(result_list)  # Create a set of unique rows
    unique_list = [list(item) for item in unique_set]  # Convert each tuple back to list

    # Get the original column names to construct the DataFrame correctly
    columns = read_risk_file.columns

    return pd.DataFrame(unique_list, columns=columns)

if __name__ == '__main__':
    read_blank_file = pd.read_csv(r'C:\Users\gtush\Desktop\Effects\risk_level\blank_sever_level.csv')
    read_risk_file = pd.read_csv(r'C:\Users\gtush\Desktop\Effects\risk_level\risk-level.csv')
    # print(read_risk_file.columns)
    blank_csv_file = data_process(read_blank_file, read_risk_file)
    blank_csv_file.to_csv(r'C:\Users\gtush\Desktop\Effects\risk_level\blank_effect.csv', index=False)
