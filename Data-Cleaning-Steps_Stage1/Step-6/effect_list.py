import pandas as pd


def effects(row, effect):
    remaining_sentence = str(row['remaining_sentence'])
    for effect_item in effect:
        if effect_item in remaining_sentence:
            return effect_item
    return None


if __name__ == '__main__':
    read_effect_list_csv = pd.read_csv(r'C:\Users\gtush\Desktop\Effects\effect_list.csv')
    effect = read_effect_list_csv['effect'].tolist()
    for i in range(1, 3):
        file_path = fr'C:\Users\gtush\Desktop\DrugBank_Set2\splits\data_cleaning_part{i}.csv'
        read_csv_file = pd.read_csv(file_path)

        read_csv_file['Effect'] = read_csv_file.apply(lambda row: effects(row, effect), axis=1)
        read_csv_file.to_csv(file_path, index=False)
        print(file_path)
