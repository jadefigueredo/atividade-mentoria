# Crie uma função chamada imprimir_multiplos que recebe dois números base e limite e imprime todos os múltiplos de base até o limite.

def imprimir_multiplos(base, limite):

    for n in range (base, limite + 1):
        if base % base == 0:
            print (n)

imprimir_multiplos (7, 9)