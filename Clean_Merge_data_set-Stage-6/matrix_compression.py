import pandas as pd
import concurrent.futures


def process_row(row):
    # Create data_list using list comprehension
    data_list = [
        f"{row[f'Dir_{i}']}{row[f'Effect_{i}']}"
        for i in range(1, 6)
        if pd.notna(row[f'Dir_{i}']) and pd.notna(row[f'Effect_{i}'])
    ]

    formatted_value = f'{data_list} | {str(row["final_severity_level"])}'

    return formatted_value


if __name__ == '__main__':
    # Read the CSV file
    input_file = r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv'
    read_file = pd.read_csv(input_file)

    # Process the first 40 rows using multithreading
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_row, row): index for index, row in read_file.iterrows()}

        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            print(index)
            formatted_value = future.result()
            read_file.at[index, 'formatted_data'] = formatted_value

    # Save the modified DataFrame to the same CSV file
    read_file.to_csv(input_file, index=False)

    print(f'File saved successfully: {input_file}')
