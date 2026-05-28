# estudando Functions 

def firsTfuct ():
    a = int(input('digite um número: '))
    b = int(input('digite outro número: '))
    c = input('digite um caractere como esses >> * % + -')
    
    if c == "*":
        cont = a * b
    
    elif c == "%":
        cont = a / b
    
    elif c == "+":
        cont = a + b
    elif c == "-":
        cont = a - b

    return cont

resultado = firsTfuct()

print(resultado)
