veiculos = ['Avião','Moto','Navio','ônibus']
f_maiuscula = lambda x: str.upper(veiculos)
nomes_maiudculos = lista(map(f_maiuscula,veiculos))
print(f'nomes={nomes_maiudculos}')