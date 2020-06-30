#### Modelos Probabilísticos de Señales y Sistemas
#### Tarea 3
#### Nombre: Jesús Rojas Barrantes
#### Carne: B46040
#### Grupo: 01



import numpy as np

from scipy import stats

import scipy.stats.mstats as ms

import matplotlib.pyplot as plt

import csv

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

import pandas as pd

from scipy.optimize import curve_fit

#Extraer los datos de una versión modificada de xy.csv sin la primera columna
xy = pd.read_csv("xy.csv")
#Convertir los datos en una matriz de valores
matriz_xy = np.array(xy.to_numpy()).astype("float")


##############################PARTE 1#############################################

#Vectores de los valores de x y y
xs = np.linspace(5, 15, num=11)
ys = np.linspace(5, 25, num=21)
#Funciones de densidad marginal de X y Y
fX = np.sum(matriz_xy, axis = 1)
fY = np.sum(matriz_xy, axis = 0)

plt.plot(xs, fX)
plt.savefig('fX.png')
plt.cla()
plt.plot(ys, fY)
plt.savefig('fY.png')

#A partir de la figura se observa que la curva pareciera ser de una distribución gaussiana
#Se define la función gaussiana
def gaussiana(x, mu, sigma):
  return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x - mu)**2/(2*sigma**2))

#Se obtienen los parámetros mu y sigma del modelo de distribución normal
paramfX, _ = curve_fit(gaussiana, xs, fX)
paramfY, _ = curve_fit(gaussiana, ys, fY)
print('Los parámetros mu y sigma para la fX son ', paramfX)
print('Los parámetros mu y sigma para la fY son ', paramfY)


##############################PARTE 2##############################################


#Dado que se asume que X y Y son independientes, la función de densidad conjunta es la multiplicación de las funciones de densidad marginales, de manera que el modelo sería.

#se define X para que no explote el codigo
xpru = 0
ypru

PMF = (1/(np.sqrt(2*np.pi*3.29944286**2)) * np.exp(-(xpru - 9.90484381)**2/(2*3.29944286**2))) * (1/(np.sqrt(2*np.pi*6.02693775**2)) * np.exp(-(ypru - 15.0794609)**2/(2*6.02693775**2)))



##############################PARTE 3#################################################

#Extraer los datos de xyp.csv y convertirlos en valores numéricos
xyp=pd.read_csv("xyp.csv")
matriz_xyp = np.array(xyp.to_numpy()).astype("float")

#A partir de la matriz generada, se obtienen los vectores respectivos de cada columna

X = matriz_xyp[: , 0]
Y = matriz_xyp[: , 1]
P = matriz_xyp[: , 2]

#Para obtener la correlación
Rxy = 0
for i in range(len(X)):
  var_x = X[i]
  var_y = Y[i]
  prob = P[i]
  Rxy = Rxy + var_x*var_y*prob

print('La correlación es: ', Rxy)


#Para obtener la covarianza
Cxy = 0
for i in range(len(X)):
  var_x = X[i]
  var_y = Y[i]
  prob = P[i]
  Cxy = Cxy + ((var_x-paramfX[0])*(var_y-paramfY[0])*(prob))
print('La covarianza es: ', Cxy )

#Para obtener el coeficiente de correlación
p = Cxy/(paramfX[1]*paramfY[1])
print('El coeficiente de correlación es: ', p)




#################PARTE 4###############################

#Para la función de densidad marginal de X
plt.cla()
plt.plot(xs, [gaussiana(i+5, paramfX[0], paramfX[1] ) for i in range(len(xs))])
plt.savefig("PMFX.png")

#Para la función de densidad marginal de Y
plt.cla()
plt.plot(ys, [gaussiana(i+5, paramfY[0], paramfY[1] ) for i in range(len(ys))])
plt.savefig("PMFY.png")

#Grafica 3D de la función de Densidad Conjunta
plt.cla()
fig = plt.figure()
ax = Axes3D(fig)
X,Y = np.meshgrid(xs,ys)
Z = (1/(np.sqrt(2*np.pi*3.29944286**2)) * np.exp(-(X - 9.90484381)**2/(2*3.29944286**2))) * (1/(np.sqrt(2*np.pi*6.02693775**2)) * np.exp(-(Y - 15.0794609)**2/(2*6.02693775**2)))
ax.plot_surface(X, Y, Z, cmap=cm.viridis)
plt.savefig("PMFconj.png")
#plt.show()