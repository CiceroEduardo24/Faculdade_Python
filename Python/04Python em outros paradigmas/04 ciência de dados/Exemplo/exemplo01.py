from sklearn import  tree
from sklearn.tree import DecisionTreeClassifier
lisa = 1
irregular = 0
pera = 1
laranja = 0

pomar =[[120,lisa],[140,lisa],[260,irregular],[380,irregular]]
resultado = [pera,pera,laranja,laranja]

#gerar uma arvore de decisão
clf = tree.DecisionTreeClassifier()

#classificador
clf = clf.fit(pomar, resultado)

peso = 220
#1 para lisa e 0 para irregular
superficie = 0

resultadousu = clf.predict([[peso,superficie]])
if resultadousu == 1:
    print('pera')
else:
    print('laranja')