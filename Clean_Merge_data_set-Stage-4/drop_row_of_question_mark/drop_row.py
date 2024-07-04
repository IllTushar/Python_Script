import pandas as pd


def data_process(read_file_csv):
    result = []
    for index, row in read_file_csv.iterrows():
        undefined = str(row['Undefinded_Code'])
        if '?' in undefined:
            pass
        else:
            result.append(row)
    return result


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Effects\risk_level\risk-level.csv'
    read_file_csv = pd.read_csv(file_path)
    # print(read_file_csv.columns)
    result = data_process(read_file_csv)
    read_file_csv = pd.DataFrame(result)
    read_file_csv = read_file_csv.drop(columns=['Undefinded_Code'])
    read_file_csv.to_csv(file_path, index=False)
