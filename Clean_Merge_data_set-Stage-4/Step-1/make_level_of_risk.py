import pandas as pd
import os


def data_process(merger_df):
    # Iterate over the merger DataFrame
    for index, row in merger_df.iterrows():
        effects = row['Effect'].split(',')
        count = 1
        for effect in effects:
            effect = effect.strip()  # Remove any surrounding whitespace
            column_name = f'severity level_{count}'
            merger_df.at[index, column_name] = effect
            count += 1

    return merger_df


if __name__ == '__main__':
    for i in range(1, 12):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        merger_file_path = file_path

        if os.path.exists(merger_file_path):
            merger_df = pd.read_csv(merger_file_path)

            # Initialize the Effect_ columns before processing
            for j in range(1, len(merger_df['Effect'].iloc[0].split(',')) + 1):
                merger_df[f'severity level_{j}'] = ""

            processed_df = data_process(merger_df)

            processed_df.to_csv(merger_file_path, index=False)
            print(f'Processed and saved: {file_path}')
        else:
            print(f'File does not exist: {file_path}')
