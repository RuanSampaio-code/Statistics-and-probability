from matplotlib.patches import Wedge
import pandas as pd
from pandas.core.indexes.base import Index
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

planilha = pd.read_csv(r'C:\Users\Ruan Sampaio\evolucaoadmit.csv')
print('=================IMPRIMINDO GRAFICO==============', '\n',planilha)
contd = 0
for x in range(0,27):
    dadosestado = planilha.iloc[x,3:12]
    print(dadosestado)
    contd = contd+1
    plt.boxplot(dadosestado, vert=1)
    plt.ylabel('Numero de admissões')
    plt.title("Boxplot do Grafico do {}º Estado".format(contd))
    plt.grid(True)
    plt.show()

