# Defina uma função chamada calcular_media que calcula a média de uma lista de números.

def verificar_primo(n):
    if n <= 1: 
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

numero = 20

resultado = verificar_primo(numero)
print(resultado)