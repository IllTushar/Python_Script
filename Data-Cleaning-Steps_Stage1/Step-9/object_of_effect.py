import pandas as pd
import re


def process_object_of_effect(sentence):
    match = re.search(r'of (.*?) can be', sentence, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


if __name__ == '__main__':
    for i in range(1, 2):
        file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
        # Read the CSV file
        read_csv_file = pd.read_csv(file_path)

        # Apply the function to the dataframe
        read_csv_file['object_of_effect'] = read_csv_file['remaining_sentence'].apply(process_object_of_effect)

        # Display the dataframe
        print(file_path)

        # # Optionally, save the modified dataframe to a new CSV file
        read_csv_file.to_csv(file_path, index=False)
