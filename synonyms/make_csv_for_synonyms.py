import pandas as pd

if __name__ == '__main__':
    synonym = ['Salbutamol', 'Florbetaben (18F)', 'Letibotulinumtoxina', 'Mirvetuximab Soravtansine', 'Rifampin',
               'Rifampicin', 'GSK-3844766A']

    df = pd.DataFrame({"synonyms": synonym})
    df.to_csv(r'C:\Users\gtush\Desktop\synonyms\synonyms_list.csv', index=False)
