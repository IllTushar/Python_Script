import pandas as pd


def data_process(merger_df):
    # Iterate over the merger DataFrame
    for index, row in merger_df.iterrows():
        for i in range(1, 6):
            direction = row[f'Dir_{i}']

            # Check if the direction is a string before splitting
            if isinstance(direction, str):
                split_data = direction.split("_")
                if len(split_data) > 1:
                    if 'anti' in split_data[-2].lower():
                        split_data[-2] = ''
                        split_data = '-' if '+' in split_data[-1] else '+'
                    elif 'cns stimulation' in split_data[-2].lower():
                        split_data[-2] = ''
                        split_data = '-' if '+' in split_data[-1] else '+'
                    elif 'decrease alertness activity' in split_data[-2].lower():
                        split_data[-2] = ''
                        split_data[-1] = '-'
                    elif 'reduced gastrointestinal motility' in split_data[-2].lower():
                        split_data[-2] = ''
                        split_data[-1] = '-'
                        split_data = split_data[-1]
                    elif 'reduced intravascular volume' in split_data[-2].lower():
                        split_data[-2] = ''
                        split_data[-1] = '-'
                        split_data = split_data[-1]
                    else:
                        split_data[-2] = ''
                        split_data = split_data[-1]
                    merger_df.at[index, f'Dir_{i}'] = ' '.join(split_data)
                else:
                    merger_df.at[index, f'Dir_{i}'] = direction
            else:
                # If direction is not a string, set it to an empty string
                merger_df.at[index, f'Dir_{i}'] = ''

    return merger_df


if __name__ == '__main__':
    for i in range(1, 15):
        file_path = fr'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\final_effect_merge_file_part{i}.csv'
        merger_df = pd.read_csv(file_path)

        processed_df = data_process(merger_df)

        processed_df.to_csv(file_path, index=False)
        print(f"Processed {file_path}")
