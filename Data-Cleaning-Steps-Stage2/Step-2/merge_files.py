import os
import pandas as pd

if __name__ == '__main__':
    read_csv_1 = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_merge_file_1.csv')
    read_csv_2 = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_merge_file_2.csv')
    final_csv = pd.concat([read_csv_1, read_csv_2], axis=0)
    final_csv.to_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv', index=False)
