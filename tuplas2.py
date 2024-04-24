# 2) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato brasileiro de futebol, na ordem de colocação, depois mostre:
# a) Apenas os primeiros 5 colocados;
# b) Os últimos 4 colocados da tabela;
# c) Uma lista com os times em ordem alfabética;
# d) Em que posição na tabela está o time do bahia.

tabela = ["Palmeiras", "Grêmio", "Atlético-MG", "Flamengo",
          "Botafogo", "Bragantino", "Fluminense", "Atlético-PR",
          "Internacional", "Fortaleza", "São Paulo", "São Paulo",
          "Cuiabá", "Corinthians", "Cruzeiro", "Vasco", "Bahia",
          "Santos", "Goiás", "Curitiba", "América-MG"]

a = tabela[0:5]
b = tabela[16:20]

print(a)
print(b)

tabela.sort()
print(tabela)