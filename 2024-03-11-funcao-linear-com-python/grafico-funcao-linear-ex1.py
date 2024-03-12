import matplotlib.pyplot as plt
import numpy as np

# Dados do problema
anos = np.array([1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000])
percent_rural = np.array([30.4, 26.4, 23.6, 21.1, 19.0, 17.1, 15.0, 13.0, 11.7, 10.5])

# Ajustando o modelo linear
coeficientes = np.polyfit(anos, percent_rural, 1)
modelo = np.poly1d(coeficientes)

estimativa_1988 = modelo(1988)
estimativa_2002 = modelo(2002)

# Plotando os dados e a linha de melhor ajuste
plt.figure(figsize=(10, 6))
plt.plot(anos, percent_rural, 'o', label='Dados Originais')
plt.plot(anos, modelo(anos), 'r--', label=f'Modelo: {modelo}')
plt.title('Percentual da População Rural da Argentina (1955-2000)')
plt.xlabel('Ano')
plt.ylabel('% Rural')
plt.legend()
plt.grid(True)
plt.show()

(estimativa_1988, estimativa_2002)
