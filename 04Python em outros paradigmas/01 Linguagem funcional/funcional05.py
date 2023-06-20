#tratando uma API
usuario={
    'nome':'joão',
    'redes':[{
        'nome':'facebook',
        'imagem_profile':"",
        'imagem_capa':"imagem1",
    },{
    'nome':'twitter',
    'imagem_profile':"imagem2",
    'imagem_capa':""
    }]
}
#retorno a imageem do profile
def get_imagem_profile(usuario):
    for rede in usuario['redes']:
        if rede[imagem_profile]:
            return rede['imagem_profile']
    return 'default'

#retorna a imagem da capa
def get_imagem_capa(usuario):
    for rede in usuario['redes']:
        if rede[imagem_capa]:
            return rede['imagem_capa']
    return 'default'

#ultilizando o partial
from functools import partial
def get_imagem(qual_imagem, usuario):
    for rede in usuario['redes']:
        if rede[qual_imagem]:
            return rede[qual_imagem]
    return 'default'

get_imagem_profile = partial(get_imagem,'imagem_profile')
get_imagem_capa = partial(get_imagem,'imagem_capa')

print('\nSaida partial final:')
print(get_imagem_profile(usuario))
print(get_imagem_capa(usuario))




