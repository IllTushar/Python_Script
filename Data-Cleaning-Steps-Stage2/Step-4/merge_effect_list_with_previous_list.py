import pandas as pd

if __name__ == '__main__':
    unique_rows = set()

    for i in range(1, 3):
        read_file_csv = pd.read_csv(fr'C:\Users\gtush\Desktop\Effects\effect_data_{i}.csv')
        # Convert each row to a tuple and add to the set
        for row in read_file_csv.itertuples(index=False, name=None):
            unique_rows.add(row)

    # Convert the set of tuples back to a DataFrame
    unique_df = pd.DataFrame(list(unique_rows), columns=read_file_csv.columns)

    # Save the unique DataFrame to a new CSV file
    unique_df.to_csv(r'C:\Users\gtush\Desktop\Effects\merge_effect.csv', index=False)

