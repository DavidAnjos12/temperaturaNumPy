import numpy as np

temperaturas = np.array([22, 21, 19, 18.5, 20.3, 25, 1])

# Calcular a média das temperaturas
media_temperatura = np.mean(temperaturas)
print(f"Média das temperaturas: {media_temperatura:.2f}°C")

# Calcular a temperatura máxima e mínima
max_temperatura = np.max(temperaturas)
min_temperatura = np.min(temperaturas)
print(f"Temperatura máxima: {max_temperatura}°C")
print(f"Temperatura mínima: {min_temperatura}°C")

# Selecionar as temperaturas acima de 21ºC
altas_temperaturas = temperaturas[temperaturas > 21]
print(f"Temperaturas acima de 21ºC: {altas_temperaturas}")