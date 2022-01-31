
from matplotlib.patches import Wedge
import pandas as pd
from pandas.core.indexes.base import Index
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

planilha = pd.read_csv(r'C:\Users\Ruan Sampaio\evolucaoadmit.csv')
print('=================IMPRIMINDO GRAFICO==============', '\n',planilha)
cont = 0
for x in range(0,27):
    dados_estado =  planilha.iloc[x,3:12]
    cont +=1
    print('Admisões do {}º Estado por meses:'.format(cont))
    print(dados_estado)
    print('\n')
    plt.bar(dados_estado.index,dados_estado.iloc[0:9])
    plt.xlabel('Meses do ano de 2021')
    plt.ylabel('Numero de admissões')
    plt.title('EVOLUÇÃO DE ADMISSOES EM CADA ESTADO BRASILEIRO \n {} º ESTADO'.format(cont))
    plt.show()
