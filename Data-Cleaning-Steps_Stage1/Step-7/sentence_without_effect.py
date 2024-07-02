import pandas as pd


def remove_effect(read_csv_file, file_path):
    # Iterate over each row in the DataFrame
    for idx, row in read_csv_file.iterrows():
        effect = str(row['Effect'])
        sentence = row['remaining_sentence']

        # Check if the effect is in the sentence and replace it
        if effect in sentence:
            read_csv_file.at[idx, 'remaining_sentence'] = sentence.replace(effect, '').strip()

    # Write the updated DataFrame back to the CSV file
    read_csv_file.to_csv(file_path, index=False)


if __name__ == '__main__':
    for i in range(1, 2):
        file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
        read_csv_file = pd.read_csv(file_path)

        remove_effect(read_csv_file, file_path)
