import pandas as pd


def data_process(read_file_csv):
    code = []
    for index, row in read_file_csv.iterrows():
        classification = row['Classification']
        if 'Moderate' in classification:
            code.append('Mo')
        elif 'Severe' in classification:
            code.append('S')
        elif 'Unknown' in classification:
            code.append('U')
        elif 'Mild' in classification:
            code.append('Mi')
        elif 'Life-threatening' in classification:
            code.append('Lt')
        else:
            code.append('')
    read_file_csv['Classification_Code'] = code
    return read_file_csv


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Effects\risk-level_1.csv'
    read_file_csv = pd.read_csv(file_path)
    df = data_process(read_file_csv)
    df.to_csv(file_path, index=False)
