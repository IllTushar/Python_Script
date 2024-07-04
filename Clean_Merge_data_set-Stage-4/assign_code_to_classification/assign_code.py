import pandas as pd


def data_process(read_file_csv):
    code = []
    for index, row in read_file_csv.iterrows():
        classification = row['Classification']
        if 'Mild' in classification:
            code.append('1')
        elif 'Moderate' in classification:
            code.append('2')
        elif 'Severe' in classification:
            code.append('3')
        elif 'Unknown' in classification:
            code.append('4')
        elif 'Life-threatening' in classification:
            code.append('5')
        else:
            code.append('')
    read_file_csv['Classification_Code'] = code
    return read_file_csv


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Effects\risk_level\risk-level.csv'
    read_file_csv = pd.read_csv(file_path)
    df = data_process(read_file_csv)
    df.to_csv(file_path, index=False)
