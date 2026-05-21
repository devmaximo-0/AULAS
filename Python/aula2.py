dicio_vazio = []


dici8 = {'nome': 'l2vision',
        'lugar': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
        'quantidade': 69
}

dici4 = {'nome': 'l2ar',
        'lugar': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
        'quantidade': 56
}

dici2 = {'nome': 'UCT',
        'lugar': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
        'quantidade': 56
}

print('~~~ SEJA BEM VINDO AO MEU PROGRAMA ~~~')
pergunta1 = input('digite a sua o nome da estação: ')
 
pergunta2 = int(input('digite a linha com APENAS "NÚMEROS": '))

# Lista com todos os dicionários
dicionarios = [dici8, dici4, dici2]

# Procura o número em todos os dicionários
encontrado = False
for dicio in dicionarios:
    if pergunta2 in dicio['lugar']:
        print(f'certinho! Número {pergunta2} encontrado na linha {dicio["nome"]}')
        encontrado = True
        break

if not encontrado:
    print('essa linha não existe na fabrica!')

pergunta3 = int(input(f'digite a quantidade de operários especializados que precisa para trabalhar na {pergunta2} na estação {pergunta1}: '))
if pergunta3 > dici2['quantidade'] or dici4['quantidade'] or dici8['quantidade']:
    print('não temos esse número aqui.')
 corretamente!')
