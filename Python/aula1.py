import json

j = []

while True:
    i = input('digite seu nome: ')

    k = input('digite sua idade: ')

    l = float(input('digite sua altura: '))

    m = int(input('digite o peso: '))

    imc = m / (l * l)

    tudo = {'nome':i, 
           'idade':k,
           'altura':l,
           'peso':m,
           'imc': imc
           }
    j.append(tudo)

    print(f"seu imc é {imc:.2f} ")

    with open('codigos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(j,arquivo, indent=4, ensure_ascii=False)


    sair = input('deseja sair ? s/n: ').lower()
    if sair == 'não' or 'n':
        j += tudo
        continue
       
    elif sair == 'sim':
     with open('codigos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(j,arquivo, indent=4, ensure_ascii=False)
        break
   
    else:
        print('responda corretamente!')
