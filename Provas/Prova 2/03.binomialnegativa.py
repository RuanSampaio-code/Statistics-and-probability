from numpy.core.fromnumeric import size
from scipy.stats import nbinom
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
from scipy.stats import binom
import seaborn as sns
from numpy import random

csv = pd.read_csv(r'C:\Users\Ruan Sampaio\coviddadosma.csv', sep=";", encoding='cp1252')
print(csv)
df = pd.DataFrame(csv)
print(df)

print('Segue o grafico da distribuição binomial negativa')
n = 10
p=0.028
X=np.array(df["Óbitos"])
x = nbinom.rvs(n,p, X)
sns.displot(x, )
plt.xlabel('Confirmados')
plt.ylabel('Probabilidade')
plt.show()
