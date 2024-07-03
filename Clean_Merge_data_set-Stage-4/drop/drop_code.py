import pandas as pd

if __name__ == '__main__':
    file_path = r"C:\Users\gtush\Desktop\Effects\risk-level_1.csv"
    read_file_code = pd.read_csv(file_path)
    read_file_code = read_file_code.drop(columns=['Classification_Code'])
    read_file_code.to_csv(file_path, index=False)
