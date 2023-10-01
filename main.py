#construindo os comando através de funções em python para uma calculadora

#função para realizar adição
def adicao(x,y):
    return x+y

#função para realizar subtração
def subtracao(x,y):
    return x-y

#função para realizar multiplicação
def multiplicacao(x,y):
    return x*y

#função para realizar divisão (tome cuidado! divisão por zero não é possível)
def divisao(x,y):
    if y == '0':
        return "Erro! Divisão por zero."
    else:
        return x/y

#Manu na tela de operações
print('Escolha uma operação matemática:')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

#Entrada do usuário
entrada = input("Digite a sua operação desejada entre as opções (1/2/3/4): ")

