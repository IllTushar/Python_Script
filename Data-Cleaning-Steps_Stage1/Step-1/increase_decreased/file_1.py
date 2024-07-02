import pandas as pd


def remove_increase_decrease(interactions):
    resultant_data_list = []
    increase_decrease_data_list = []

    for interaction in interactions:
        original_interaction = interaction
        if 'increased' in interaction:
            interaction = interaction.replace('increased', '').strip()
            increase_decrease_data_list.append('increased')
        elif 'decreased' in interaction:
            interaction = interaction.replace('decreased', '').strip()
            increase_decrease_data_list.append('decreased')
        elif 'increase' in interaction:
            interaction = interaction.replace('increase', '').strip()
            increase_decrease_data_list.append('increased')
        elif 'decrease' in interaction:
            interaction = interaction.replace('decrease', '').strip()
            increase_decrease_data_list.append('decreased')
        elif 'reduced' in interaction:
            interaction = interaction.replace('reduced', '').strip()
            increase_decrease_data_list.append('decreased')
        else:
            increase_decrease_data_list.append('')

        if interaction != original_interaction:
            resultant_data_list.append(interaction)
        else:
            resultant_data_list.append(original_interaction)

    return resultant_data_list, increase_decrease_data_list


def replace_drug_in_sentence(row):
    drug_name = row['Drug']
    sentence = row['remaining_sentence']
    if drug_name in sentence:
        return sentence.replace(drug_name, '').strip()
    return sentence


if __name__ == '__main__':
    for i in range(1, 2):
        file_path = fr'C:\Users\gtush\Desktop\drug_cleaning\splits\final_set_{i}.csv'
        read_csv_file = pd.read_csv(file_path)
        # Drop base drug column
        # read_csv_file = read_csv_file.drop(columns=['sentence_without_drug'])

        interactions = read_csv_file['Interaction']

        sentence, increase_decrease = remove_increase_decrease(interactions)

        read_csv_file['remaining_sentence'] = sentence
        read_csv_file['Direction'] = increase_decrease
        # # Apply the function to each row and create a new column 'new_remain_sentence'
        # read_csv_file['sentence_without_drug'] = read_csv_file.apply(replace_drug_in_sentence, axis=1)
        read_csv_file.to_csv(file_path,index=False)
        print("file ", file_path)
