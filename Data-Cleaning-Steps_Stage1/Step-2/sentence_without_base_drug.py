import pandas as pd


def remove_salt_name(read_csv_file):
    base_drug = read_csv_file['Base Drug']
    remaining_sentence = read_csv_file['remaining_sentence']

    if base_drug in remaining_sentence:
        return remaining_sentence.replace(base_drug, '').strip()
    return remaining_sentence


if __name__ == '__main__':
    for i in range(1, 2):
        file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
        read_csv_file = pd.read_csv(file_path)

        read_csv_file['sentence_without_base_drug'] = read_csv_file.apply(remove_salt_name, axis=1)

        read_csv_file.to_csv(file_path,index=False)
        print(file_path)
