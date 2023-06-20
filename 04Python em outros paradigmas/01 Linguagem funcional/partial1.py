#exemplo partial
import operator
from _functools import partial
adicina_um = partial(operator.add,1)

print(adicina_um(5))

#Segundo exemplo
import collections
from operator import attrgetter
pessoa = collections.namedtuple('Pessoa','nome idade')
pessoas = [pessoa('joão',44),pessoa('Ana',26)]

print(sorted(pessoas,key=attrgetter('nome')))
print(sorted(pessoas,key=attrgetter('idade')))

#terceiro exemplo
from functools import partial
sort_nome = partial(sorted,key=attrgetter('nome'))
sort_idade = partial(sorted, key=attrgetter('idade'))

print(sort_nome(pessoas))
print(sort_idade(pessoas))

