# Crie uma função chamada verificar_vogal que recebe uma letra como entrada e retorna se ela é uma vogal ou não.

def verifica_vogal():
    letra = str(input("Digite qualquer letra do alfabeto: "))
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print("Esta letra é uma vogal.")
    else:
        print("Esta letra não é uma vogal.")

verifica_vogal()