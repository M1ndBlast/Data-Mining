import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

data = pd.read_csv('VC.txt', header=1, delim_whitespace=True)
x = data.iloc[:,0].values
y = data.iloc[:,1].values

print(data)

plt.plot(x,y, 'ro')
plt.xlabel('Carreras')
plt.ylabel('Turnos al bat')
plt.show()

# Ajuste de datos a polinomio de primer grado
# Creara la pendiente y la ordenada al origen
coeficientes = np.polyfit(x,y,1)
polinomio = np.poly1d(coeficientes)
print(polinomio)


# Posteriormente realizar la interpretacion de los datos
# hablar sobre la desviacion estandar, etc,. Tambien de los datos a tipicos



# Tarea: Investigar en la libreria de  statsmodels que funciones hay, para que sirven, sintexis, como cargar los datos, etc.