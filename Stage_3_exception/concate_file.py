import pandas as pd

if __name__ == '__main__':
    read_csv_1 = pd.read_csv(r'C:\Users\gtush\Desktop\Effects\final_Effect_Cleaned.csv')
    read_csv_2 = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\none_effect_set_2.csv')
    list = [read_csv_1, read_csv_2]
    df = pd.concat(objs=list, axis=0)
    df.to_csv(r'C:\Users\gtush\Desktop\Effects\final_Effect_Cleaned.csv', index=False)
