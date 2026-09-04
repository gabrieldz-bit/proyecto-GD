import matplotlib.pyplot as plt

municipios = ["Cali", "Alcalá", "Andalucía", "Buga", "Cartago"]
bovinos = [9272, 11578, 6796, 15432, 12350]

cd C:/Users/gabri/Documents/proyecto1




# Gráfica de línea
plt.plot(municipios, bovinos)   # Línea que conecta los puntos
plt.title("Inventario bovino por municipio")
plt.xlabel("Municipios")
plt.ylabel("Número de bovinos")
plt.show()

# Gráfica de barras
plt.bar(municipios, bovinos)   # Barras verticales
plt.title("Inventario bovino por municipio")
plt.xlabel("Municipios")
plt.ylabel("Número de bovinos")
plt.show()
