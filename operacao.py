import math
import string


class Operacao: #Nome de classe sempre em letra maiúcula
    def __init__(self):  #Classe construtora - self é tipo o this
        self.num1 = 0  #Inicializando variáveis, sempre que ter uma nova variável precisa colocar aqui, ex: num3.
        self.num2 = 0

    def coletar(self, num1, num2): #Vai coletar os dados digitados para usar nas demais funções
        self.num1 = num1
        self.num2 = num2


    def somar(self, num1, num2):
        self.coletar(num1, num2)  # usando a def coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2<=0:                 #Sempre colocar : (dois pontos) para dizer que um método vai começar.
            return "Divisão Inválida!"
        else:
            return self.num1 / self.num2

    def tabuada(self,num1):
        resultado = ""
        for i in range(0,11,1):  # O número 0 é o número que irá começar, o 11 é a quantidade de repetições e o 1 é de quantos em quantos números ele vai fazer.
            resultado += f' \n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self,base,expoente):
        return pow(base,expoente) #pow funciona para fazer potencia e é um método que funciona sozinho

    def raiz (self, num):
        return math.sqrt(num) #Alguns métodos precisam usar o math, como é o caso de sqrt e ela precisa ser importada.

    def imprimir(self):
        resultado = ""
        for i in range(0, 10, 1):
            resultado += f' \n {i+1}'
        return resultado

    def pares(self):
        resultado = ""
        for i in range(1, 21, 1):
            if i % 2 == 0:
                resultado += f' \n  {i}'
        return resultado

    def soma(self):
        resultado = 0
        for i in range(0,100,1):
            resultado += i + 1
        return resultado

    def multiplos(self):
        resultado = ""
        for i in range(0, 11,1):
            resultado += f' \n{5} * {i} = {5 * i}'
        return resultado

    def parouimpar(self, num1):

        if num1 % 2 == 0:
            return "O número é PAR."
        else:
            return "O número é IMPAR"

    def numero(self, num1):
        if num1 == 0:
            return "O número é ZERO."
        elif num1>0:
            return "O número é POSITIVO"
        else:
            return"O número é NEGATIVO"

    def ate(self,num1):
        resultado = ""
        for i in range(0, num1, 1):
            resultado += f' \n {i + 1}'
        return resultado

    def somatodos(self,num1):
        resultado = 0
        for i in range(0,num1,1):
            resultado += i + 1
        return resultado

    def impares(self):
        resultado = ""
        for i in range(1, 21, 1):
            if i % 2 != 0:
                resultado += f' \n  {i}'
        return resultado

    def primo(self,num1):
        if num1==2:
            return "É primo!"
        elif num1==3:
            return "É primo!"
        elif num1 == 5:
            return "É primo!"
        elif num1 == 7:
            return "É primo!"
        elif num1 % 2 != 0:
            if num1 % 3 !=0:
                 if num1 % 5 != 0:
                       if num1 % 7 != 0:
                             return "É primo!"

        else:
            return "Não é primo!"

    def primoMostrar(self, num1):
        if num1 == 2:
            return num1
        elif num1 == 3:
            return num1
        elif num1 == 5:
            return num1
        elif num1 == 7:
            return num1
        elif num1 % 2 != 0:
            if num1 % 3 != 0:
                if num1 % 5 != 0:
                    if num1 % 7 != 0:
                        return num1


    def fatorial(self, num1):
        resultado = 1
        for i in range(1, num1+1):
            resultado *=i
        return resultado

    def fibonacci(self,num1):
        sequence=[0,1]
        while len (sequence)< num1:
            next_number = sequence [-1] + sequence[-2]
            sequence.append(next_number)
        return sequence

    def digitos(self,num1):
        tamanho = len(str(num1))
        palavra = str(num1)
        soma = 0
        for i in range(0, tamanho, 1):
            soma += int(palavra[i])
        return soma

    def imprimirtodos(self,num1):
            resultado = ""
            for i in range(0, num1, 1):
                resultado += f' \n {i + 1}'
            return resultado


    def imprimirprimos(self,num1):
        resultado = ""
        for i in range(0, num1, 1):
            resultado += f'\n{self.primoMostrar(i)}'
        return resultado


    def collatz(self,num1):
        if num1 % 2 == 0:
            resultado = num1/2
        else:
            resultado = (num1*3)+1

        return resultado+1

    def somatodos2(self, num1):
        resultado = 0
        for i in range(0, num1, 1):
            resultado += i + 1
        return resultado

    def perfeito(self,num1):
        soma = 0
        for val in range (1,num1):
            if num1 % val == 0:
                soma += val
        if soma == num1:
            return "É perfeito"
        else:
            return "Não é perfeito"











