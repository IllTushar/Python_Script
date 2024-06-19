import pandas as pd
from datetime import datetime as dt


def filter_effect(interactions):
    directions = []
    for interaction in interactions:
        if 'increased' in interaction:
            directions.append("increased")
        elif 'decreased' in interaction:
            directions.append('decreased')
        elif 'increase' in interaction:
            directions.append('increased')
        elif 'decrease' in interaction:
            directions.append('decreased')
        elif 'reduced' in interaction:
            directions.append('decreased')
        else:
            directions.append('')  # Handle cases where no keyword is found
    return directions


if __name__ == '__main__':
    total_time_start = dt.now()
    print("Total time start", total_time_start)

    for i in range(1, 1081):
        file_path = fr'C:\Users\gtush\Desktop\CSV Collection_1\separation_{i}.csv'
        print(file_path)
        read_csv_drug_bank = pd.read_csv(file_path)
        # read_csv_drug_bank = read_csv_drug_bank.drop(columns=['Effect'])
        directions = filter_effect(read_csv_drug_bank["Interaction"])
        read_csv_drug_bank['Direction'] = directions
        read_csv_drug_bank.to_csv(file_path, index=False)

    total_time_end = dt.now()
    print("Total time end", total_time_end)
    time_diff = total_time_end - total_time_start
    print("Total diff", time_diff)
