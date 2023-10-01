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

#Verificação da escolha do usuário
if entrada in ['1','2','3','4']:
    #são duas variáveis para fazer as operações
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if entrada == '1':
        print("Resultado: ", adicao(num1,num2))
    elif entrada == '2':
        print("Resultado: ", subtracao(num1,num2))
    elif entrada == '3':
        print("Resultado: ", multiplicacao(num1,num2))
    elif entrada == '4':
        print("Resultado: ", divisao(num1,num2))

else:
    print("Escolha inválida. Por favor, escolha uma opção válida entre adição (1), subtração (2), multiplicação (3) e divisão (4)")
