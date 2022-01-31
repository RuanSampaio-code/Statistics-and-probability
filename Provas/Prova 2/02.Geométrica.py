from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom
from scipy.stats import binom
import seaborn as sns
from numpy import random

csv = pd.read_csv(r'C:\Users\Ruan Sampaio\export.csv')

#distribuição geometrica 
df = pd.DataFrame(csv)
print(df)
X=np.array(df['casos_acumulados'])
p=0.5
funcao = geom.pmf(X,p)
fig,ax=plt.subplots(1,1,figsize=(8,6))
plt.ylabel("Probabilidade",fontsize="18")
plt.xlabel("Nº de ensaios",fontsize="18")
plt.title("Distribuição Geo - No. de ensaio  Vs Probab", fontsize="18")
ax.vlines(X, 0, funcao, colors='r', lw=5, alpha=0.5)
plt.show()

