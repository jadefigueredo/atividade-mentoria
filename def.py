# Defina uma função chamada calcular_media que calcula a média de uma lista de números.

def calcula_media(lista):
    total = sum(lista)
    media = total / len(lista)
    return media

numeros = [10, 16, 17, 23, 45]

media_resultado = calcula_media(numeros)

print(f"A média dos números é: {media_resultado}")