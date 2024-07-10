import pandas as pd
import numpy as np

if __name__ == '__main__':
    # Load the main file
    read_main_file = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv')

    # Load the rows and columns
    base_drug = pd.read_csv(r'C:\Users\gtush\Desktop\matrix\rows.csv')
    rows = base_drug['Base Drug'].tolist()

    drug = pd.read_csv(r'C:\Users\gtush\Desktop\matrix\columns.csv')
    columns = drug['Drug'].tolist()

    # Initialize the matrix with empty strings
    matrix = np.full((len(rows), len(columns)), '', dtype=object)

    # Fill the matrix
    for index, row in read_main_file.iterrows():
        BaseDrug = row['BaseDrugCode']
        Drug = row['DrugCode']

        if BaseDrug in rows and Drug in columns:
            row_index = rows.index(BaseDrug)
            col_index = columns.index(Drug)
            matrix[row_index, col_index] = row['formatted_data']

    # Convert the matrix to a DataFrame for better visualization
    matrix_df = pd.DataFrame(matrix, index=rows, columns=columns)
    matrix_df.to_csv(r'C:\Users\gtush\Desktop\matrix\compress.csv')
