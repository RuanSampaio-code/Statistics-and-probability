import matplotlib
from matplotlib import colors
from matplotlib.patches import Wedge
import pandas as pd
from pandas.core.indexes.base import Index
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

planilha = pd.read_csv(r'C:\Users\Ruan Sampaio\evolucaoadmit.csv')
print('=================IMPRIMINDO GRAFICO==============', '\n',planilha)

cont = 0
for r in range(0,27):
    cont = cont+1
    dadosestado = planilha.iloc[r,3:12]
    print(dadosestado)
    somatotal = dadosestado.sum()
    print('O total dos 100% =',somatotal)
    print(dadosestado/somatotal)
    eixox = dadosestado.index
    eixoy = (somatotal/somatotal)  #dadosestado[2]/28102
    plt.bar(dadosestado.index,(dadosestado/somatotal)*100)
    plt.title('Distribuição de probabilidade, Grafico {}º estado '.format(cont))
    plt.ylabel('Porcentagem % ')
    plt.xlabel('Meses')
    plt.show()
