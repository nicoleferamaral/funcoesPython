# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.

#O python usa a identação para separar e precisar ser de um TAB de distância.

#from operacao import Operacao
# Conecta a main com a classe, quando eu for querer pegar apenas uma função em específico, apenas colocar o nome da função ex: from operacao import Somar.

from menu import Menu

if __name__ == '__main__':
        men = Menu()
        men.executar()



        #opera = Operacao() #Nome para representar a classe Operacao
       # num1 = int(input("Informe o primeiro número: "))  #Como o input é texto, coloca o int para informar que irá receber números
        #num2 = int(input("Informe o segundo número: "))
        #print(f'\nA soma dos números é: {opera.somar(num1, num2)}')
        #print(f'A subtração dos números é: {opera.subtrair(num1, num2)}')
        #print(f'A divisão dos números é: {opera.dividir(num1, num2)}')
        #print(f'A multiplicação dos números é: {opera.multiplicar(num1, num2)}')
        #print(f'\nA tabuada do {num1} é: {opera.tabuada(num1)}')
        #print(f'\nA tabuada do {num2} é: {opera.tabuada(num2)}')
        #print(f'\nO resultado da potência é: {opera.potencia(num1,num2)}')
        #print(f'A raiz de {num1} é: {opera.raiz(num1)}')
        #print(f'A raiz de {num2} é: {opera.raiz(num2)}')