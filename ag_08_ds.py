# Pesquisa de Satisfacao - Empresa TudoWeb

from mimetypes import init
from operator import add
from py_compile import main


print("======================================")
print(" PESQUISA DE SATISFACAO - TUDOWEB")
print("======================================")

# Inicializacao dos contadores
excelente = 0
bom = 0
ruim = 0

# Repeticao para entrevistar 50 pessoas
for i in range(1, 51):

    print("\nEntrevistado", i)

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("\nComo voce avalia nosso atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opcao: "))

    # Estrutura de decisao
    if opiniao == 1:
        excelente += 1
        print("Opiniao registrada: EXCELENTE")

    elif opiniao == 2:
        bom += 1
        print("Opiniao registrada: BOM")

    elif opiniao == 3:
        ruim += 1
        print("Opiniao registrada: RUIM")

    else:
        print("Opcao invalida!")

# Exibicao dos resultados
print("\n======================================")
print(" RESULTADO FINAL DA PESQUISA")
print("======================================")

print("Total de respostas EXCELENTE:", excelente)
print("Total de respostas BOM:", bom)
print("Total de respostas RUIM:", ruim)

print("======================================")