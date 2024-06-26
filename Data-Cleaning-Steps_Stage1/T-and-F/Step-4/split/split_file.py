import pandas as pd


# Function to split the CSV file
def split_csv(file_path, chunk_size=100000):
    # Read the CSV file in chunks
    for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
        print(file_path)
        chunk.to_csv(f'{file_path.split(".")[0]}_part{i + 1}.csv', index=False)


if __name__ == '__main__':
    file_path = r'C:\Users\gtush\Desktop\DrugBank_Set2\Complete2.csv'
    # Call the function to split the CSV file
    split_csv(file_path)
