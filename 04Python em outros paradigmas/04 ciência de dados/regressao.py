import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas

#############  Algoritmo Supervisionado  ###############
"""
Supervisionado – regressão linear
Neste exemplo, utilizaremos uma série histórica fictícia de casos de dengue de uma determinada cidade e,
 com o auxílio do algoritmo supervisionado de regressão linear, predizeremos casos futuros.
A série está em uma planilha (arquivo CSV) com duas colunas, ano e casos (número de casos).
Na planilha, temos o número de casos de 2001 a 2017. Utilizaremos essa série histórica e aplicaremos
 o algoritmo de regressão linear para estimar os casos de dengue para o ano de 2018.
"""
#############      Pré-processamento     ###############
# Coleta e Integração
arquivo = pandas.read_csv('dados_dengue.csv')

anos = arquivo[['ano']]
casos = arquivo[['casos']]

##############       Mineração        #################
regr = LinearRegression()
regr.fit(X=anos, y=casos)

ano_futuro = [[2018]]
casos_2018 = regr.predict(ano_futuro)

print('Casos previstos para 2018 ->', int(casos_2018))

############      Pós-processamento     ################
plt.scatter(anos, casos, color='black')
plt.scatter(ano_futuro, casos_2018, color='red')
plt.plot(anos, regr.predict(anos), color='blue')

plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([2018])
plt.yticks([int(casos_2018)])

plt.show()