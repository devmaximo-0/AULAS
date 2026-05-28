def calcimpost(valor):
    if valor < 1000:
        imposto = valor * 0.01
    elif valor < 2000:
        imposto = valor * 0.05
    elif valor < 3000:
        imposto = valor * 0.15
    return imposto

primeiro_valor = 2500
resultado = calcimpost(primeiro_valor)
print(resultado)
