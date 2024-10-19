import pandas as pd
from my_scopiy import find_intervents


name = ['Гістероскопія','Езофагогастродуоденоскопія',
        'Колоноскопія','Цистоскопія','Бронхоскопія']
mn = [{'35630-00','35633-01'}, 
      {'30473-00', '30473-05', '30473-07', '30473-08', '30473-01', '30473-06'},
      {'32090-00', '32084-00', '32084-02', '32084-01', '32087-00', '32090-01',
       '32090-02', '32093-00'},
      {'36803-00', '36812-00', '36806-00', '36836-00'},
      {'41889-01', '41889-05', '38418-06', '41898-04'}]

path = "./raw/"
df = pd.read_csv(path)
df['group'] = df['actions'].apply(find_intervents, mn=mn, name=name)
df.to_excel('./out/scopiy.xlsx', index=False)
