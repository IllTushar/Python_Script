import pandas as pd

if __name__ == '__main__':
    read_csv = pd.read_csv(r'C:\Users\gtush\Desktop\Effects\total_effects_in_approved.csv')

    read_csv['Clean Sentence'] = read_csv['Clean Sentence'].str.replace('Serum Concentration',
                                                                           'Serum concentration')
    read_csv.to_csv(r'C:\Users\gtush\Desktop\Effects\total_effects_in_approved.csv', index=False)
