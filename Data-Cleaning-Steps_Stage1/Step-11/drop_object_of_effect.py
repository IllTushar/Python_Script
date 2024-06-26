import pandas as pd

if __name__ == '__main__':
    for i in range(1, 3):
        file_path = fr'C:\Users\gtush\Desktop\DrugBank_Set2\splits\data_cleaning_part{i}.csv'
        read_csv_file = pd.read_csv(file_path)
        print(file_path)

        read_csv_file = read_csv_file.drop(columns=['object_of_effect'])

        read_csv_file.to_csv(file_path, index=False)
