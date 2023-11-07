import math

from operacao import Operacao

class Soma(Operacao):

    def calcular(self, num1: float, num2:float):
         soma = num1 + num2
         return f'{num1} + {num2} = {soma}'

class Subtracao(Operacao):
     
     def calcular(self, num1: float, num2:float):
        resultado = num1 - num2
        return f'{num1} - {num2} = {resultado}'
     
class Multiplicacao(Operacao):

    def calcular(self, num1: float, num2: float):
        resultado = num1 * num2
        return f'{num1} x {num2} = {resultado}'

class Divisao(Operacao):
    
    def calcular(self, num1: float, num2: float):
        resultado = num1 / num2
        return f'{num1} / {num2} = {resultado}'

class Potenciacao(Operacao):
    
    def calcular(self, num1: float, num2: float):
        resultado = num1 ** num2  
        return f'{num1} ** {num2} = {resultado}'

class Raiz(Operacao):
    
    def calcular(self, num: float, num2: float = None):
        raiz_quadrada = math.sqrt(num)
        return f'A raiz de {num} é {raiz_quadrada}'
    
class Logaritimo(Operacao):

    def calcular(self, num_x: float, num_base: float):
        logaritimo = math.log(num_x, num_base)
        return f'O logaritimo de número {num_x} na base {num_base} é {logaritimo}'