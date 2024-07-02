import pandas as pd

if __name__ == '__main__':
    read_csv_file = pd.read_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\none_effect_1.csv')
    data_set = set()
    for effect in read_csv_file['Effect']:
        data_set.add(effect)
    df = pd.DataFrame({"Cleaned_Effect": list(data_set)})
    df.to_csv(r'C:\Users\gtush\Desktop\Merge_Set3orSet4\effect_splits\none_effect_set_2.csv', index=False)
