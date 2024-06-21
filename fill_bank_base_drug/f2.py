import pandas as pd


def filter_sentence(read_csv):
    # Iterate over the rows of the DataFrame
    for index, row in read_csv.iterrows():
        # Check if 'ethyl' is in the sentence and the corresponding Base_drug cell is empty
        if 'ethyl' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            # Replace 'ethyl' with ''
            new_sentence = row['sentence_without_base_drug'].replace('ethyl', '')
            # Assign the new sentence back to the DataFrame
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            # Set 'Icosapent ethyl' in the corresponding Base_drug cell
            read_csv.at[index, 'Base_drug'] = 'Icosapent ethyl'

        elif 'Salbutamol' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('Salbutamol', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Salbutamol'

        elif 'acetate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('acetate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Eslicarbazepine acetate'

        elif 'enacarbil' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('enacarbil', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Gabapentin enacarbil'

        elif 'Florbetaben (18F)' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('Florbetaben (18F)', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Florbetaben F-18'

        elif 'salicylate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('salicylate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Choline salicylate'

        elif 'gluconate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('gluconate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Chromium gluconate'

        elif 'nicotinate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('nicotinate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Chromium nicotinate'

        elif 'lauroxil' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('lauroxil', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Aripiprazole lauroxil'

        elif 'besylate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('besylate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Atracurium besylate'

        elif 'dienanthate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('dienanthate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Estradiol dienanthate'

        elif 'benzoate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('benzoate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Estradiol benzoate'

        elif 'furoate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('furoate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Fluticasone furoate'

        elif 'butyrate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('butyrate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Hydrocortisone butyrate'

        elif 'tetrahydrate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('tetrahydrate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Magnesium acetate tetrahydrate'

        elif 'cation' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('cation', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Magnesium cation'

        elif 'phosphate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('phosphate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Hydrocortisone phosphate'

        elif 'citrate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('citrate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Magnesium citrate'

        elif 'glycinate' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('glycinate', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Magnesium glycinate'

        elif 'hydroxide' in row['sentence_without_base_drug'] and pd.isna(row['Base_drug']):
            new_sentence = row['sentence_without_base_drug'].replace('hydroxide', '')
            read_csv.at[index, 'sentence_without_base_drug'] = new_sentence
            read_csv.at[index, 'Base_drug'] = 'Magnesium hydroxide'

        else:
            pass


if __name__ == '__main__':
    for i in range(792, 1081):
        # Read the CSV file
        read_csv = pd.read_csv(fr'C:\Users\gtush\Desktop\sample\separation_{i}.csv')

        # Apply the filter_sentence function
        filter_sentence(read_csv)
        # Save the modified DataFrame back to CSV
        read_csv.to_csv(fr'C:\Users\gtush\Desktop\sample_output\separation_{i}.csv', index=False)
        print(fr'C:\Users\gtush\Desktop\sample_output\separation_{i}.csv')
