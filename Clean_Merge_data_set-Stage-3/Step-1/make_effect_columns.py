import pandas as pd


def data_process(cleaner_df, merger_df):
    # Create a dictionary for quick lookup from the cleaner DataFrame
    clean_dict = cleaner_df.set_index('Dirty')['Cleaned'].to_dict()

    # Iterate over the merger DataFrame
    for index, row in merger_df.iterrows():
        effects = row['Effect'].split(',')
        count = 1
        for effect in effects:
            effect = effect.strip()  # Remove any surrounding whitespace
            if effect in clean_dict:
                column_name = f'Effect_{count}'
                merger_df.at[index, column_name] = clean_dict[effect]
                count += 1

    return merger_df


if __name__ == '__main__':
    cleaner_file_path = r'C:\Users\gtush\Desktop\data_cleaning\Effects_Cleaner.csv'
    cleaner_df = pd.read_csv(cleaner_file_path)

    merger_file_path = r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv'
    merger_df = pd.read_csv(merger_file_path)

    processed_df = data_process(cleaner_df, merger_df)

    processed_df.to_csv(merger_file_path, index=False)
    print(processed_df)
