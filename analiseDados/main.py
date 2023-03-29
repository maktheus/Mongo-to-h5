import pandas as pd
import matplotlib.pyplot as plt

# carregar os dados em um dataframe do pandas
df = pd.read_csv('../saida/hex/payloadHex.csv', index_col='Time')
print(df)
# gerar gráfico de linha para cada coluna com o valor máximo
df.max().plot(kind='line')
plt.title('Valor máximo')
plt.savefig("valorMaximo.png")

# gerar gráfico de linha para cada coluna com o valor mínimo
df.min().plot(kind='line')
plt.title('Valor mínimo')
plt.savefig("valorMinimo.png")

# gerar gráfico de linha para cada coluna com a média dos valores
df.mean().plot(kind='line')
plt.title('Valor médio')
plt.savefig("valorMedio.png")

# gerar gráfico de linha para cada coluna com a mediana dos valores
df.median().plot(kind='line')
plt.title('Valor mediano')
plt.savefig("valorMediano.png")

# gerar gráfico de linha para cada coluna com o desvio padrão dos valores
df.std().plot(kind='line')
plt.title('Desvio padrão')
plt.savefig("desvioPadrao.png")

# gerar gráfico de linha para cada coluna com a variância dos valores
df.var().plot(kind='line')
plt.title('Variância')
plt.savefig("variancia.png")

# gerar gráfico de linha para cada coluna com a amplitude dos valores
(df.max() - df.min()).plot(kind='line')
plt.title('Amplitude')
plt.savefig("amplitude.png")

# gerar gráfico de linha para cada coluna com a amplitude interquartil dos valores
(df.quantile(0.75) - df.quantile(0.25)).plot(kind='line')
plt.title('Amplitude interquartil')
plt.savefig("amplitudeInterquartil.png")


# gerar gráfico de linha para cada coluna com o coeficiente de variação dos valores
(df.std() / df.mean()).plot(kind='line')
plt.title('Coeficiente de variação')
plt.savefig("coeficienteVariacao.png")

# gerar gráfico de linha para cada coluna com o coeficiente de assimetria dos valores
((df.mean() - df.median()) / df.std()).plot(kind='line')
plt.title('Coeficiente de assimetria')
plt.savefig("coeficienteAssimetria.png")

# gerar gráfico de linha para cada coluna com o coeficiente de curtose dos valores
((df.mean() - df.median()) / df.std()).plot(kind='line')
plt.title('Coeficiente de curtose')
plt.savefig("coeficienteCurtose.png")

# gerar gráfico de linha para cada coluna com o coeficiente de assimetria dos valores
((df.mean() - df.median()) / df.std()).plot(kind='line')
plt.title('Coeficiente de assimetria')
plt.savefig("coeficienteAssimetria.png")