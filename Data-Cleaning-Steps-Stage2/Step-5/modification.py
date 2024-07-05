import pandas as pd


def data_process(read_csv):
    for index, row in read_csv.iterrows():
        effect = row['Effect']
        direction = row['Direction']
        if ', anti-angiogenesis' not in effect and 'anti' or 'Anti' in effect:
            if 'increased' in direction:
                read_csv.at[index, 'Direction'] = direction.replace('increased', 'decreased')
            elif 'decreased' in direction:
                read_csv.at[index, 'Direction'] = direction.replace('decreased', 'increased')

            read_csv.at[index, 'Effect'] = effect.replace("anti", '').replace("Anti", '')

        elif 'CNS stimulation' in effect:
            if 'increased' in direction:
                read_csv.at[index, 'Direction'] = direction.replace('increased', 'decreased')
            elif 'decreased' in direction:
                read_csv.at[index, 'Direction'] = direction.replace('decreased', 'increased')

            read_csv.at[index, 'Effect'] = effect.replace('CNS stimulation', 'CNS Depression')

        elif 'Decreased alertness activities' in effect:
            read_csv.at[index, 'Direction'] = direction.replace('increased', 'decreased')
            read_csv.at[index, 'Effect'] = effect.replace('Decreased alertness activities', 'alertness activities')

        elif 'reduced gastrointestinal motility' in effect:
            read_csv.at[index, 'Direction'] = direction.replace('increased', 'decreased')
            read_csv.at[index, 'Effect'] = effect.replace("reduced", '')

        elif 'reduced intravascular volume' in effect:
            read_csv.at[index, 'Direction'] = direction.replace('increased', 'decreased')
            read_csv.at[index, 'Effect'] = effect.replace("reduced", '')

        else:
            pass
    return read_csv


if __name__ == '__main__':
    for i in range(1, 15):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        read_csv_file = pd.read_csv(file_path)
        df = data_process(read_csv_file)
        df.to_csv(file_path, index=False)
        print(file_path)
