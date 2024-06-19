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
            increase_decrease_data_list.append('increase')
        elif 'decrease' in interaction:
            interaction = interaction.replace('decrease', '').strip()
            increase_decrease_data_list.append('decrease')
        else:
            increase_decrease_data_list.append('')

        if interaction != original_interaction:
            resultant_data_list.append(interaction)
        else:
            resultant_data_list.append(original_interaction)

    return resultant_data_list, increase_decrease_data_list


if __name__ == '__main__':
    read_csv_file = pd.read_csv(r'C:\Users\gtush\Desktop\split_files\split_file_1.csv')
    interactions = read_csv_file['Interaction']

    sentence, increase_decrease = remove_increase_decrease(interactions)

    read_csv_file['remaining_sentence'] = sentence
    read_csv_file['Effect'] = increase_decrease

    read_csv_file.to_csv(r'C:\Users\gtush\Desktop\CSV Collection\separation_1.csv', index=False)
