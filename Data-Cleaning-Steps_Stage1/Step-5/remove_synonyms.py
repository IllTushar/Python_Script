import pandas as pd


def remove_synonyms(read_synonyms_file_csv, read_file):
    remaining_sentence_list = []
    for row in read_file['remaining_sentence']:
        sentence = row
        for synonyms in read_synonyms_file_csv['synonyms'].tolist():
            sentence = sentence.replace(synonyms, "").strip()
        remaining_sentence_list.append(sentence)

    return remaining_sentence_list


if __name__ == '__main__':
    synonyms_file_path = r'C:\Users\gtush\Desktop\synonyms\synonyms_list.csv'
    read_synonyms_file_csv = pd.read_csv(synonyms_file_path)

    for i in range(1, 2):
        file_path_csv = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
        read_file = pd.read_csv(file_path_csv)

        remaining_sentence = remove_synonyms(read_synonyms_file_csv, read_file)

        read_file['remaining_sentence'] = remaining_sentence
        read_file.to_csv(file_path_csv, index=False)
