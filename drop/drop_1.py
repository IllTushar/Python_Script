import pandas as pd

if __name__ == '__main__':
    for i in range(1, 591):
        read_csv_file = pd.read_csv(fr'C:\Users\gtush\Desktop\sample_output\separation_{i}.csv')
        print(fr'C:\Users\gtush\Desktop\sample_output\separation_{i}.csv')
        read_csv_file = read_csv_file.drop(columns=['sentence_without_drug'])
        read_csv_file.to_csv(fr'C:\Users\gtush\Desktop\sample_output\separation_{i}.csv', index=False)

