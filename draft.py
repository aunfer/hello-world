# eh_multiplo_10 = lambda x: x%10==0
# print(eh_multiplo_10(22))


# def fatorial (n):
#     for i in range (1,n):
#         n=n*i
#     return n

# print(fatorial(4))


# nome_completo=str(input("Digite o nome completo: "))

# def primeiro_nome(nome_completo):
#     nome_completo=nome_completo.split(" ")
#     print(nome_completo[:1])
# primeiro_nome(nome_completo)


# nomes=["Joao Carlos", "Ana Clara", "Maria Eduarda"]
# def primeiro_nome(grupo):
#     for pessoa in grupo:
#         nome=pessoa.split(" ")
#         print(nome[:1])
# primeiro_nome(nomes)

from datetime import date, datetime

def funcao(data):
    data=datetime.strptime(data,"%d/%m/%Y")
    formatado = data.strftime("%A")
    return formatado
print(funcao(input("Digite uma data: ")))