import matplotlib.pyplot as plt
import numpy as np

# Função para visualização gráfica
def plotar_funcao(func, x_range, titulo='', xlabel='x', ylabel='f(x)', legenda=''):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = func(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=legenda or titulo)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    if legenda:
        plt.legend()
    plt.show()

# Funções essenciais
def funcao_linear(x):
    return 2 * x + 3

plotar_funcao(funcao_linear, [-10, 10],"Função Linear", legenda="f(x) = 2x + 3")
