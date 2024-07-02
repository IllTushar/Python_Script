import pandas as pd
import os


def data_process(df):
    # Fill missing values in 'Effect_1' column with 'the active metabolites of'
    df['Effect_1'].fillna('the active metabolites of', inplace=True)
    return df


if __name__ == '__main__':
    base_path = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits'
    for i in range(1, 15):
        file_name = f'final_effect_merge_file_part{i}.csv'
        file_path = os.path.join(base_path, file_name)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Process the data
        df = data_process(df)

        # Save the processed data back to CSV
        df.to_csv(file_path, index=False)

        print(f'Processed file: {file_path}')
