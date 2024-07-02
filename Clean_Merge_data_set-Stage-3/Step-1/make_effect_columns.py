import pandas as pd
import os


def data_process(cleaner_df, merger_df):
    # Create a dictionary for quick lookup from the cleaner DataFrame using indices
    clean_dict = cleaner_df['Cleaned_Effect'].to_dict()

    # Iterate over the merger DataFrame
    for index, row in merger_df.iterrows():
        effects = row['Effect'].split(',')
        count = 1
        for effect in effects:
            effect = effect.strip()  # Remove any surrounding whitespace
            if effect in clean_dict.values():
                column_name = f'Effect_{count}'
                merger_df.at[index, column_name] = effect
                count += 1

    return merger_df


if __name__ == '__main__':
    cleaner_file_path = r'C:\Users\gtush\Desktop\Effects\final_Effect_Cleaned.csv'
    cleaner_df = pd.read_csv(cleaner_file_path)

    for i in range(1, 15):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        merger_file_path = file_path

        if os.path.exists(merger_file_path):
            merger_df = pd.read_csv(merger_file_path)

            # Initialize the Effect_ columns before processing
            for j in range(1, len(merger_df['Effect'].iloc[0].split(',')) + 1):
                merger_df[f'Effect_{j}'] = ""

            processed_df = data_process(cleaner_df, merger_df)

            processed_df.to_csv(merger_file_path, index=False)
            print(f'Processed and saved: {file_path}')
        else:
            print(f'File does not exist: {file_path}')
