"""
Utilizar o modelo de regressão lógística treinado para fazer a classificação
"""
from exercicio04 import*
previsto = pipe.predict(x_teste[0].reshape(-1,1))
real = y_teste[0]
print('previsto:{}; Real:{};'.format(previsto[0],real))