import pandas as pd

if __name__ == '__main__':
    cleaner_file_path = r'C:\Users\gtush\Desktop\data_cleaning\Effects_Cleaner.csv'
    read_clear_file = pd.read_csv(cleaner_file_path)
    data = set()
    for i in read_clear_file['Cleaned']:
        data.add(i)
    df = pd.DataFrame({"Cleaned_Effect": list(data)})
    df.to_csv(r'C:\Users\gtush\Desktop\data_cleaning\Effects_Cleaner_With_Code.csv', index=False)
