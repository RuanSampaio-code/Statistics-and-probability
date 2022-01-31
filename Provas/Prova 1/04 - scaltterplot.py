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


est = planilha["Estado"]
#print(est)

contd1 = 1; contd2 = 2;  
contd3 = 3; contd4 = 4;
contd5 = 5; contd6 = 6;
contd7 = 7; contd8 = 8;
contd9 = 9; contd10 = 10;
contd11 = 11; contd12 = 12;
contd13 = 13; contd14 = 14;
contd15 = 15; contd16 = 16;
contd17 = 17; contd18 = 18;
contd19 = 19; contd20 = 20;
contd21 = 21; contd22 = 22;
contd23 = 23; contd24 = 24;
contd25 = 25; contd26 = 26;

contd1 = 1
#GRAFICOS DO 1º ESTADO
for m in range(1,27): 
        contd1 = contd1+1
        plt.scatter(planilha.iloc[0,3:12],planilha.iloc[m,3:12])
        plt.title('Grafico Scattplot comparando 1º estado com o {}º Estado'.format(contd1))
        plt.show()
#GRAFICOS DO 2º ESTADO
for m in range(2,27):
    contd2 = contd2+1      
    plt.scatter(planilha.iloc[1,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 2º estado com o {}º'.format(contd2))
    plt.show()

#GRAFICOS DO 3º ESTADO
for m in range(3,27):
    contd3 = contd3+1      
    plt.scatter(planilha.iloc[2,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 3º estado com o {}º'.format(contd3))
    plt.show() 

#GRAFICOS DO 4º ESTADO 
for m in range(4,27):
    contd4 = contd4+1      
    plt.scatter(planilha.iloc[3,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 4º estado com o {}º'.format(contd4))
    plt.show() 

#GRAFICOS DO 5º ESTADO 

for m in range(5,27):
    contd5 = contd5+1      
    plt.scatter(planilha.iloc[4,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 5º estado com o {}º'.format(contd5))
    plt.show()

#GRAFICOS DO 6º ESTADO 
for m in range(6,27):
    contd6 = contd6+1      
    plt.scatter(planilha.iloc[5,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 6º estado com o {}º'.format(contd6))
    plt.show()

#GRAFICOS DO 7º ESTADO 
for m in range(7,27):
    contd7 = contd7+1      
    plt.scatter(planilha.iloc[6,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 7º estado com o {}º'.format(contd7))
    plt.show()

#GRAFICOS DO 8º ESTADO 
for m in range(8,27):
    contd8 = contd8+1      
    plt.scatter(planilha.iloc[7,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 8º estado com o {}º'.format(contd8))
    plt.show()

#GRAFICOS DO 9º ESTADO 
for m in range(9,27):
    contd9 = contd9+1      
    plt.scatter(planilha.iloc[8,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 9º estado com o {}º'.format(contd9))
    plt.show()

#GRAFICOS DO 10º ESTADO 

for m in range(10,27):
    contd10 = contd10+1      
    plt.scatter(planilha.iloc[9,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 10º estado com o {}º'.format(contd10))
    plt.show()


#GRAFICOS DO 11º ESTADO 

for m in range(11,27):
    contd11 = contd11+1      
    plt.scatter(planilha.iloc[10,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 11º estado com o {}º'.format(contd11))
    plt.show()

#GRAFICOS DO 12º ESTADO 

for m in range(12,27):
    contd12 = contd12+1      
    plt.scatter(planilha.iloc[11,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 12º estado com o {}º'.format(contd12))
    plt.show()

#GRAFICOS DO 13º ESTADO 

for m in range(13,27):
    contd13 = contd13+1      
    plt.scatter(planilha.iloc[12,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 13º estado com o {}º'.format(contd13))
    plt.show()

#GRAFICOS DO 14º ESTADO 

for m in range(14,27):
    contd14 = contd14+1      
    plt.scatter(planilha.iloc[13,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 14º estado com o {}º'.format(contd14))
    plt.show()

#GRAFICOS DO 15º ESTADO 
for m in range(15,27):
    contd15 = contd15+1      
    plt.scatter(planilha.iloc[14,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 15º estado com o {}º'.format(contd15))
    plt.show()

#GRAFICOS DO 16º ESTADO 
for m in range(16,27):
    contd16 = contd16+1      
    plt.scatter(planilha.iloc[15,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 16º estado com o {}º'.format(contd16))
    plt.show()

#GRAFICOS DO 17º ESTADO 
for m in range(17,27):
    contd17 = contd17+1      
    plt.scatter(planilha.iloc[16,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 17º estado com o {}º Estado'.format(contd17))
    plt.show()

#GRAFICOS DO 18º ESTADO 
for m in range(18,27):
    contd18 = contd18+1      
    plt.scatter(planilha.iloc[17,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 18º estado com o {}º'.format(contd18))
    plt.show()

#GRAFICOS DO 19º ESTADO 
for m in range(19,27):
    contd19 = contd19+1      
    plt.scatter(planilha.iloc[18,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 19º estado com o {}º'.format(contd19))
    plt.show()

#GRAFICOS DO 20º ESTADO 
for m in range(20,27):
    contd20 = contd20+1  
    plt.scatter(planilha.iloc[19,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 20º estado com o {}º'.format(contd20))
    plt.show()

#GRAFICOS DO 21º ESTADO 
for m in range(21,27):
    contd21 = contd21+1      
    plt.scatter(planilha.iloc[20,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 21º estado com o {}º'.format(contd21))
    plt.show()

#GRAFICOS DO 22º ESTADO 
for m in range(22,27):
    contd22 = contd22+1      
    plt.scatter(planilha.iloc[21,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 22º estado com o {}º'.format(contd22))
    plt.show()

#GRAFICOS DO 23º ESTADO 
for m in range(23,27):
    contd23 = contd23+1      
    plt.scatter(planilha.iloc[22,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 23º estado com o {}º'.format(contd23))
    plt.show()

#GRAFICOS DO 24º ESTADO 
for m in range(24,27):
    contd24 = contd24+1
    plt.scatter(planilha.iloc[23,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 24º estado com o {}º'.format(contd24))
    plt.show()

#GRAFICOS DO 25º ESTADO 
for m in range(25,27):
    contd25 = contd25+1  
    plt.scatter(planilha.iloc[24,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 25º estado com o {}º'.format(contd25))
    plt.show()

#GRAFICOS DO 26º ESTADO 
for m in range(26,27):
    contd26 = contd26+1      
    plt.scatter(planilha.iloc[25,3:12],planilha.iloc[m,3:12])
    plt.title('Grafico Scattplot comparando 26º estado com o {}º'.format(contd26))
    plt.show()
