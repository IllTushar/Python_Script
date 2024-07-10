import pandas as pd

if __name__ == '__main__':
    read_csv_file = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\final_effect_merge_file.csv')
    base_drug = {i for i in read_csv_file['Drug']}
    df = pd.DataFrame({"Drug": list(base_drug)})
    df.to_csv(r'C:\Users\gtush\Desktop\matrix\columns.csv', index=False)
