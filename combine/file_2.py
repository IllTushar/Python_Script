import pandas as pd
from datetime import datetime as dt


def filter_base_drug_name(read_csv_drug_bank, read_csv_interaction):
    list_base_drug_name = []
    new_sentence_list = []

    # Extract the list of drug names
    drug_names = read_csv_drug_bank['Name'].tolist()

    # Iterate over each interaction sentence
    for interaction in read_csv_interaction['sentence_without_drug']:
        temp = None
        new_sentence = interaction

        for drug_name in drug_names:
            if drug_name in interaction:
                temp = drug_name
                new_sentence = interaction.replace(drug_name, "").strip()
                break  # Stop after finding the first match

        if temp:
            new_sentence_list.append(new_sentence)
            list_base_drug_name.append(temp)
        else:
            new_sentence_list.append(interaction)  # No match found
            list_base_drug_name.append(None)  # No drug found

    return new_sentence_list, list_base_drug_name


if __name__ == '__main__':
    total_time_start = dt.now()
    print("Total time start ", total_time_start)
    read_csv_drug_bank = pd.read_csv(r'C:\Users\gtush\Desktop\DrugBankData\sorted_name_dec.csv')

    for i in range(6, 51):
        read_csv_interaction = pd.read_csv(fr'C:\Users\gtush\Desktop\CSV Collection_1\separation_{i}.csv')

        time_start = dt.now()
        print("time start", time_start)
        read_csv_interaction = read_csv_interaction.drop(columns=['remaining_sentence'])

        new_sentence, base_drug = filter_base_drug_name(read_csv_drug_bank, read_csv_interaction)

        read_csv_interaction['Base_drug'] = base_drug
        read_csv_interaction['sentence_without_base_drug'] = new_sentence

        read_csv_interaction.to_csv(fr'C:\Users\gtush\Desktop\Collection_2\separation_{i}.csv', index=False)
        print(fr'C:\Users\gtush\Desktop\Collection_2\separation_{i}.csv')

        time_end = dt.now()
        print("time end", time_end)
        time_diff = time_end - time_start
        print("Time diff:", time_diff)

    total_time_end = dt.now()
    print("total time end ", total_time_end)
    total_time_diff = total_time_end - total_time_start
    print("Total time diff ", total_time_diff)
