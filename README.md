# Tarea3
Jesús Rojas Barrantes
B46040
Grupo 01

# Pregunta 1.

Para determinar la curva de mejor ajuste para cada funcion de densidad marginal, fue necesario obtener de los datos las siguientes gráficas.

https://raw.githubusercontent.com/JRB-08/Tarea3/master/fX.png

https://raw.githubusercontent.com/JRB-08/Tarea3/master/fY.png

Obsevando ambas figuras, se determina que la cuvra de mejor ajuste es una distribución gaussiana. De ella se obtiene que:

Los parámetros mu y sigma para la fX son  9.90484381 y 3.29944286 respectivamente, mientras que para fY son 15.0794609 y 6.02693775..

PMFX = (1/(np.sqrt(2*np.pi*3.29944286**2)) * np.exp(-(X - 9.90484381)**2/(2*3.29944286**2)))

PMFY = (1/(np.sqrt(2*np.pi*6.02693775**2)) * np.exp(-(Y - 15.0794609)**2/(2*6.02693775**2)))




# Pregunta 2.

Dado que se asume independecia entre X y Y, la función de densidad conjunta es la multiplicación de las funciones de densidad marginales.

PMF = (1/(np.sqrt(2*np.pi*3.29944286**2)) * np.exp(-(X - 9.90484381)**2/(2*3.29944286**2))) * (1/(np.sqrt(2*np.pi*6.02693775**2)) * np.exp(-(Y - 15.0794609)**2/(2*6.02693775**2)))

# Pregunta 3
A partir de los datos suministraods en el documento xyp.csv se obtuvieron los siguientes datos


-La correlación es:  149.54281000000012

-La covarianza es:  0.06669156997881567

-El coeficiente de correlación es:  0.0033537726852568696


# Pregunta 4

Gráfica de la Función de Densidad Marginal de X

https://raw.githubusercontent.com/JRB-08/Tarea3/master/PMFX.png


Gráfica de la Función de Densidad Marginal de Y

https://raw.githubusercontent.com/JRB-08/Tarea3/master/PMFY.png


Gráfica de la Función de Densidad Conjunta

https://raw.githubusercontent.com/JRB-08/Tarea3/master/PMFconj.png



