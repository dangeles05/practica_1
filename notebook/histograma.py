import matplotlib.pyplot as plt 

marcas_clase = [1,2,3,4,5,6]
frecuencias = [440,790,580,740,630,330]

marcas_texto = ["chicken meat", "cow's meat", "vegetables", "fish", "jam", "pork meat"]
plt.figure(figsize = (12,6))

plt.bar(marcas_clase, frecuencias, 
        width = 1, edgecolor = "k",
       color = {"#44DAA5", "#2F9773", "#7873C5", "#C59573", "#B9C573", "#C57384"})

plt.xticks(marcas_clase, marcas_texto, fontsize = 15, rotation = 45)
##plt.xlabel("Marcas de clase", fontsize = 20)
plt.ylabel("Calories", fontsize = 20)
plt.title("Sandwich's type", fontsize = 25)
plt.grid()
plt.show()