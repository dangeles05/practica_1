import matplotlib.pyplot as plt
import numpy as np

marcas_clase = [1, 2, 3, 4, 5, 6]
frecuencias = [440, 790, 580, 740, 630, 330]

total_frecuencias = np.cumsum(frecuencias)  # Calcula las frecuencias acumuladas

marcas_texto = ["chicken meat", "cow's meat", "vegetables", "fish", "jam", "pork meat"]
datos_x = [0]+ marcas_clase
datos_y = [0]+ frecuencias
plt.figure(figsize=(12, 6))

plt.plot(datos_x, datos_y, 
        linewidth = 5, color = "r", linestyle = ":", 
        marker = "v", markersize = 15, markerfacecolor = "y", markeredgecolor = "b")

plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)
plt.ylabel("Acumulative Frequencies", fontsize=20)
plt.title("Sandwich's Type", fontsize=25)
plt.grid()
plt.show()