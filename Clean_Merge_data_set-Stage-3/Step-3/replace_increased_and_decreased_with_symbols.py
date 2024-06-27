import pandas as pd


def process_symbols(read_csv):
    for index, row in read_csv.iterrows():
        direction = row['Direction']
        if 'increased' in direction:
            new_dir = direction.replace('increased', '+').strip()
            # read_csv.at[index,]


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv'
    read_csv = pd.read_csv(file_path)
    process_symbols(read_csv)
