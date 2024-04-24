# if... elif

# Escreva uma função chamada classificar_numero que recebe um número como argumento e retorna uma mensagem indicando se o número é positivo, negativo ou zero.


def classificar_numero():
    numero = int(input("Digite qualquer número, positivo, negativo ou inteiro: "))
    if numero > 0:
        print("Este número é positivo!")
    elif numero < 0:
        print ("Este número é negativo!")
    else:
        print("Este número é zero!")

classificar_numero()
