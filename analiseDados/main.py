import pandas as pd
import matplotlib.pyplot as plt

# carregar os dados em um dataframe do pandas
df = pd.read_csv('saida/hex/payloadHex.csv')

# gerar gráfico de linha para cada coluna com o valor máximo
df.max().plot(kind='line')
plt.title('Valor máximo')
plt.show()

# gerar gráfico de linha para cada coluna com o valor mínimo
df.min().plot(kind='line')
plt.title('Valor mínimo')
plt.show()

# gerar gráfico de linha para cada coluna com a média dos valores
df.mean().plot(kind='line')
plt.title('Valor médio')
plt.show()
