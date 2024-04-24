# Escreva uma função chamada soma_pares que recebe um número inteiro positivo n e retorna a soma dos números pares de 0 até n.

def soma_pares():
    n = int(input("Digite um número inteiro: "))
    soma = 0
    
    for numero in range(n + 1):
        if numero % 2 == 0:
            soma+= numero

    print("A soma dos números pares até", n, "é", soma)
soma_pares()