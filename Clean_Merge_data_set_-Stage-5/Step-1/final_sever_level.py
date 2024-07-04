import pandas as pd


def data_process(read_csv_file):
    for index, row in read_csv_file.iterrows():
        # Initialize the data variable to hold the maximum severity level found
        data = None

        for i in range(1, 6):
            col = row.get(f'severity level_{i}')
            if col is not None:
                try:
                    col = float(col)  # Convert to float
                except ValueError:
                    # Skip non-numeric values
                    continue

                if data is None:
                    data = col
                else:
                    data = max(data, col)

        # Assign the maximum severity level found to 'final_severity_level'
        read_csv_file.at[index, 'final_severity_level'] = data

    return read_csv_file


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv'
    read_csv_file = pd.read_csv(file_path)

    read_csv_file = data_process(read_csv_file)
    read_csv_file.to_csv(file_path, index=False)
