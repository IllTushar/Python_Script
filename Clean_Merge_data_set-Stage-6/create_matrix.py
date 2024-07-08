import pandas as pd

if __name__ == '__main__':
    read_file = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv')
    # print(read_file.columns)
    matrix_drug = read_file['Drug'].unique()
    matrix_base_drug = read_file['Base Drug'].unique()
    matrix = pd.DataFrame(columns=matrix_drug, index=matrix_base_drug)
    matrix.to_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\matrix.csv')
