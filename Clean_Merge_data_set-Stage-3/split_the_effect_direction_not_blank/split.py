import pandas as pd


def process_data(read_csv):
    not_none_effect = read_csv[~read_csv['Direction'].isna()]
    return not_none_effect


if __name__ == '__main__':
    read_csv = pd.read_csv(r'C:\Users\gtush\Desktop\Effects\Effects_Cleaned.csv')
    effects = process_data(read_csv)
    effects.to_csv(r'C:\Users\gtush\Desktop\Effects\exp_effects.csv', index=False)
