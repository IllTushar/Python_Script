import pandas as pd

if __name__ == '__main__':
    cleaner_file_path = r'C:\Users\gtush\Desktop\Effects\Effects_Cleaned.csv'
    read_clear_file = pd.read_csv(cleaner_file_path)
    data = set()
    for i in read_clear_file['Merged String']:
        data.add(i)
    df = pd.DataFrame({"Cleaned_Effect": list(data)})
    df.to_csv(r'C:\Users\gtush\Desktop\Effects\final_Effect_Cleaned.csv', index=False)
