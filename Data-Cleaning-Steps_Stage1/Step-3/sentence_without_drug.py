import pandas as pd


def remove_drug(read_csv_file):
    drug_name = read_csv_file['Drug']
    sentence = read_csv_file['sentence_without_base_drug']

    if drug_name in sentence:
        return sentence.replace(drug_name, '').strip()
    return sentence


if __name__ == '__main__':
    for i in range(1, 2):
        file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
        read_csv_file = pd.read_csv(file_path)

        read_csv_file['remaining_sentence'] = read_csv_file.apply(remove_drug, axis=1)

        read_csv_file.to_csv(
            file_path,
            index=False)
        print(file_path)
