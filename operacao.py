from abc import ABC, abstractmethod
import math

class Operacao(ABC):
    
    @abstractmethod
    def calcular(self, num1: float, num2: float = None) -> str:
        pass