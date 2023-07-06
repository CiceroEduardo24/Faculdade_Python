"""
Ultilizar o modelo de Regressão Logística
"""
from sklearn.model_selection import train_test_split
from exercicio03 import *
x_treino, x_teste, y_treino, y_teste = train_test_split(digitos.data,
                                                        digitos.target,
                                                        test_size=25,
                                                        random_state=0)
from sklearn.linear_model import  LogisticRegression
from sklearn.pipeline import  make_pipeline
from sklearn.preprocessing import StandardScaler
pipe = make_pipeline(StandardScaler(),
                     LogisticRegression())
pipe.fit(x_treino,y_treino)