import pandas as pd 
import seaborn as sns
import matplotlib as plt
df = pd.read_csv(r'C:\Users\Ruan Sampaio\evolucaoadmit.csv')
print('=================IMPRIMINDO GRAFICO==============', '\n',df)
estado = df.loc[0]
print(estado)
media = int(estado.iloc[3:11].mean())
mediana= int(estado.iloc[3:11].median())
print(media)
print(mediana)

