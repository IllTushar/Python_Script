import pandas as pd


def replace_drug_in_sentence(row):
    drug_name = row['Drug']
    sentence = row['remaining_sentence']
    if drug_name in sentence:
        return sentence.replace(drug_name, '').strip()
    return sentence


if __name__ == '__main__':
    read_csv_file = pd.read_csv(r'C:\Users\gtush\Desktop\CSV Collection\separation_1.csv')
    # Drop base drug column
    read_csv_file = read_csv_file.drop(columns=['Base Drug'])
    # Apply the function to each row and create a new column 'new_remain_sentence'
    read_csv_file['sentence_without_drug'] = read_csv_file.apply(replace_drug_in_sentence, axis=1)
    read_csv_file.to_csv(r'C:\Users\gtush\Desktop\CSV Collection\separation_1.csv', index=False)
