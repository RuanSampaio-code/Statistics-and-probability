import matplotlib
from matplotlib import colors
from matplotlib.patches import Wedge
import pandas as pd
from pandas.core.indexes.base import Index
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

planilha = pd.read_csv(r'C:\Users\Ruan Sampaio\evolucaoadmit.csv')
print('=================IMPRIMINDO PLANILHA==============', '\n',planilha)

dadosestado = planilha.iloc[0:26,3:12]  #FATIAMENTO DE PLANILHA
estadomaior = dadosestado.max() #valores do estado com maior media
mediamaior = estadomaior.mean() #media do estado com maior numero

#media do estado com maior media
print('Valores dos meses do Estado com maior media:\n',estadomaior)
print('Media do estado com maior nº de admissçes é igual a', mediamaior)
print('A probablidade de ter um estado com media de admissões menor que São Paulo é 100%,\npois nenhum estado tem media maior que o estado de São paulo. ')

