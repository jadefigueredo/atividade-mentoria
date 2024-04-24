# 1) Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.

numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco",
                   "seis", "sete", "oito", "nove", "dez", "onze",
                   "doze", "treze", "quatorze", "quinze", "dezesseis",
                   "dezessete", "dezoito", "dezenove", "vinte")
while True:
  numero_inteiro = int(input("Digite um número inteiro de 1 a 20: "))
  if 0 <= numero_inteiro <= 20:
    break
  print("Tente novamente.", end = "")
print(f"Você digitou o número {numeros_extenso[numero_inteiro]}")

while True:
  continuar = str(input("Deseja continuar? Digite Sim ou Não."))
  if continuar == "Sim":
    continue
  else:
    break