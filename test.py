import pandas as pd

start_data_num = 0
label = 'Health'
file_path = r'dataset\gearset\Health_30_2.csv'
df = pd.read_csv(file_path, sep='\t', skiprows=16 + start_data_num, nrows=256)
df = df.dropna(axis=1, how='all')

datas = df.values

print(datas[:, 2])
