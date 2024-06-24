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

    return increase_decrease_data_list


if __name__ == '__main__':

    for i in range(1, 9):
        file_path = fr'C:\Users\gtush\Desktop\FinalCsv\complete_file_splits\complete_extract_data_file2_part{i}.csv'
        read_csv_file = pd.read_csv(file_path)
        print(file_path)
        interactions = read_csv_file['Interaction']

        increase_decrease = remove_increase_decrease(interactions)

        read_csv_file['Direction'] = increase_decrease

        read_csv_file.to_csv(file_path, index=False)
