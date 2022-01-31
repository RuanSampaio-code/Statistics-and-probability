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
print('======DIVISÃO QUATÍLICA DOS ESTADOS======')
for d in range(0,27):
    cont +=1
    dadosestado = planilha.iloc[d,3:12]
    divquart= np.quantile(dadosestado, [0.25,0.5,0.75])
    print('{}º estado = {}'.format(cont, divquart))