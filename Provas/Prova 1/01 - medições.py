

from matplotlib.patches import Wedge
import pandas as pd
from pandas.core.indexes.base import Index
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

planilha = pd.read_csv(r'C:\Users\Ruan Sampaio\evolucaoadmit.csv')
print('=================IMPRIMINDO PLANILHA ==============', '\n',planilha)

contador=0
for n in range(0,27):
    contador = contador+1
    print('==============DADOS DO',contador,'º ESTADO=============== ', '\n')
    print('INFORMAÇÕES SOBRE AS ADMISSÕES DE CADA ESTADO:')
    dadosestado = planilha.iloc[n,3:12]    
    media_est = int(dadosestado.mean())
    mediana_est = int(dadosestado.median())
    desvio_est = int(dadosestado.std())
    print(' - A media de admissoes: ',media_est)
    print(' - A mediana de admissoes: ',mediana_est)
    print(' - Desvio padrão: ',desvio_est)
    print('\n')


