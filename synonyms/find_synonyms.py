import pandas as pd


def list_sentence_contains_synonyms(read_csv):
    sentence_list = []
    which_not_present = []
    category = []
    for index, row in read_csv.iterrows():
        if row['Base Drug'] not in row['Interaction']:
            sentence_list.append(row['Interaction'])
            which_not_present.append(row['Base Drug'])
            category.append('Base Drug')
        if row['Drug'] not in row['Interaction']:
            sentence_list.append(row['Interaction'])
            which_not_present.append(row['Drug'])
            category.append('Drug')

    return sentence_list, which_not_present, category


if __name__ == '__main__':
    for i in range(1, 9):
        file_path = fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file2_part{i}.csv'

        read_file_csv = pd.read_csv(file_path)

        # Apply the function to each row and flatten the list of lists
        sentences, not_present, category = list_sentence_contains_synonyms(read_file_csv)

        # Create a DataFrame from the resulting sentences
        df = pd.DataFrame({'Sentence': sentences, "Not Present": not_present, "Category": category})

        # Drop empty rows if there are any
        df = df.dropna().reset_index(drop=True)

        # Save the DataFrame to a new CSV file
        output_path = fr'C:\Users\gtush\Desktop\FinalCsv\synonyms\synonyms_file{i}.csv'
        df.to_csv(output_path, index=False)

        print(output_path)
