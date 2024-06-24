import pandas as pd


def remove_drug(read_csv_file):
    drug_name = read_csv_file['Drug']
    sentence = read_csv_file['sentence_without_base_drug']

    if drug_name in sentence:
        return sentence.replace(drug_name, '').strip()
    return sentence


if __name__ == '__main__':
    for i in range(1, 9):
        read_csv_file = pd.read_csv(
            fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file_part{i}.csv')

        read_csv_file['remaining_sentence'] = read_csv_file.apply(remove_drug, axis=1)

        read_csv_file.to_csv(
            fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file_part{i}.csv',
            index=False)
        print(fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file_part{i}.csv')
