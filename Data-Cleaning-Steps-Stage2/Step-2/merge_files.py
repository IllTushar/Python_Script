import os
import pandas as pd

if __name__ == '__main__':
    read_csv_1 = pd.read_csv(r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\Complete1.csv')
    read_csv_2 = pd.read_csv(r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\Complete2.csv')
    final_csv = pd.concat([read_csv_1, read_csv_2], axis=0)
    final_csv.to_csv(r'C:\Users\gtush\Desktop\Data_Cleaning_stage_2\merge_file.csv', index=False)
