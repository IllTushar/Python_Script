import pandas as pd


def data_process(cleaner_df, merger_df):
    # Create a dictionary for quick lookup from the cleaner DataFrame
    clean_dict = cleaner_df.set_index('Unmerged String')['Merged String'].to_dict()

    # Iterate over the merger DataFrame
    for index, row in merger_df.iterrows():
        effects = row['Effect'].split(',')
        direction = row['Direction']
        count = 1
        for effect in effects:
            effect = effect.strip()  # Remove any surrounding whitespace
            if effect in clean_dict:
                column_name = f'Dir_{count}'
                merger_df.at[index, column_name] = clean_dict[effect] + "_" + direction
                count += 1

    return merger_df


if __name__ == '__main__':
    cleaner_file_path = r'C:\Users\gtush\Desktop\Effects\Effects_Cleaned.csv'
    cleaner_df = pd.read_csv(cleaner_file_path)
    for i in range(1, 15):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        merger_file_path = file_path
        merger_df = pd.read_csv(merger_file_path)

        processed_df = data_process(cleaner_df, merger_df)

        processed_df.to_csv(merger_file_path, index=False)
        print(file_path)
