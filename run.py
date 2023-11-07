from operacoes import Soma, Subtracao ,Divisao , Multiplicacao, Potenciacao, Raiz, Logaritimo
from operacao import Operacao
import math


def menu():
    print('\n')
    print('                                                             -----------')
    print('                                                             Calculadora')
    print('                                                             -----------')
    print('\n')

    print('--------------------')
    print('ESCOLHA UMA OPERAÇÃO')
    print('--------------------')
    print('''
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        5 - Potenciação
        6 - Raiz quadrada
        7 - Logaritmo              
    ''')
    escolhendo_operacao = int(input('Digite um número de acordo com a operação desejada: '))
    print('')

    return escolhendo_operacao


def calculadora(escolhendo_operacao):    
    if escolhendo_operacao == 1:
        calculo = Soma()
        print('Escolha os dois valores')
        num1 = float(input('      Primeiro valor: '))
        num2 = float(input('      Segundo valor: '))
        resultado = calculo.calcular(num1, num2)
        print('------------')
        print(resultado)
        print('------------')
    
    elif escolhendo_operacao == 2:
        calculo = Subtracao()
        print('Escolha os dois valores')
        num1 = float(input('      Primeiro valor: '))
        num2 = float(input('      Segundo valor: '))
        resultado = calculo.calcular(num1, num2)
        print('------------')
        print(resultado)
        print('------------')

    elif escolhendo_operacao == 3:
        calculo = Multiplicacao()
        print('Escolha os dois valores')
        num1 = float(input('      Primeiro valor: '))
        num2 = float(input('      Segundo valor: '))
        resultado = calculo.calcular(num1, num2)
        print('------------')
        print(resultado)
        print('------------')

    elif escolhendo_operacao == 4:
        calculo = Divisao()
        print('Escolha os dois valores')
        num1 = float(input('      Primeiro valor: '))
        num2 = float(input('      Segundo valor: '))
        resultado = calculo.calcular(num1, num2)
        print('------------')
        print(resultado)
        print('------------')

    elif escolhendo_operacao == 5:
        calculo = Potenciacao()
        print('Escolha os dois valores')
        num1 = float(input('      Primeiro valor: '))
        num2 = float(input('      Segundo valor: '))
        resultado = calculo.calcular(num1, num2)
        print('------------')
        print(resultado)     
        print('------------')       

    elif escolhendo_operacao == 6:
        calculo = Raiz()
        print('Escolha o valor')
        num1 = float(input('      Primeiro valor: '))
        resultado = calculo.calcular(num1)
        print('------------')
        print(resultado)
        print('------------')

    elif escolhendo_operacao == 7:
        calculo = Logaritimo()
        print('Escolha os dois valores')
        num1 = float(input('      Primeiro valor: '))
        num2 = float(input('      Segundo valor: '))
        resultado = calculo.calcular(num1, num2)
        print('------------')
        print(resultado)
        print('------------')

    else:
        print('Algo deu errado, tente novamente...')   

if __name__=='__main__':
    command = 'sim'
    while command == 'sim':
        menu()
        escolhendo_operacao = int(input('Digite um número de acordo com a operação desejada: '))
        calculadora(escolhendo_operacao)
        command = input('Deseja continuar usando a calculadora?\n(sim/não):').lower()

    

    
