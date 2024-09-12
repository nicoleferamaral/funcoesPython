from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarmenu(self):
        print('\n ------ MENU ------\n\n'
              + '\n0. Sair'
              + '\n1. Somar'
              + '\n2. Subtrair'
              + '\n3. Dividir'
              + '\n4. Multiplicar'
              + '\n5. Potência'
              + '\n6. Raiz'
              + '\n7. Tabuada'
              + '\n8. Imprimir 1 ao 10'
              + '\n9. Imprimir pares 1 ao 20'
              + '\n10. Somar do 1 ao 100'
              + '\n11. Tabuada do 5'
              + '\n12. Par ou Impar'
              + '\n13. Positivo, Negativo ou Zero'
              + '\n14. Imprimir 1 ao número'
              + '\n15. Somar do 1 até o número'
              + '\n16. Imprimir ímpares 1 ao 20'
              + '\n17. Primo'
              + '\n18. Fatorial'
              + '\n19. Fibonacci'
              + '\n20. Somar dígitos'
              + '\n21. Pares e ímpares'
              + '\n22. Imprimir primos'
              + '\n23. Somar todos'
              + '\n24. Sequencia de Collatz'
              + '\n25. Número perfeito'

              )


    def coletar(self):

        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))


    def executar(self):
        while self.opcao != 0:
            self.mostrarmenu()
            self.opcao = int(input('Escolha uma das opções do MENU: '))

            if self.opcao == 0:
                print('Obrigado!')
            elif self.opcao == 1:
                self.coletar() #Chamando o input
                print(f'\nA soma dos números é: {self.opera.somar(self.num1, self.num2)}')

            elif self.opcao == 2:      #ELIF é o mesmo que else if
                self.coletar()
                print(f'\nA subtração dos números é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'\nA divisão dos números é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'\nA multiplicação dos números é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'\nA potência dos números é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'\nA raiz do {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'\nA raiz do {self.num2} é: {self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'\nA tabuada do {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:

                print(f'\n {self.opera.imprimir()}')

            elif self.opcao == 9:

                print(f'\n {self.opera.pares()}')

            elif self.opcao == 10:

                print(f'\nA soma do 1 ao 100 é {self.opera.soma()}')

            elif self.opcao == 11:

                print(f'\nTabuada do 5 \n{self.opera.multiplos()}')

            elif self.opcao == 12:
                self.coletar()
                print(f'\nPar ou Impar \n{self.opera.parouimpar(self.num1)}')
                print(f'\nPar ou Impar \n{self.opera.parouimpar(self.num2)}')

            elif self.opcao == 13:
                self.coletar()
                print(f' \n{self.opera.numero(self.num1)}')
                print(f' \n{self.opera.numero(self.num2)}')

            elif self.opcao == 14:
                self.coletar()
                print(f'\n {self.opera.ate(self.num1)}')
                print(f'\n {self.opera.ate(self.num2)}')

            elif self.opcao == 15:
                self.coletar()
                print(f'\nA soma do 1 ao {self.num1} é \n{self.opera.somatodos(self.num1)}')
                print(f'\nA soma do 1 ao {self.num2} é \n{self.opera.somatodos(self.num2)}')

            elif self.opcao == 16:

                print(f'\n {self.opera.impares()}')

            elif self.opcao == 17:
                self.coletar()
                print(f' \n{self.opera.primo(self.num1)}')
                print(f' \n{self.opera.primo(self.num2)}')

            elif self.opcao == 18:
                self.coletar()
                print(f'\n O fatorial de {self.num1} é {self.opera.fatorial(self.num1)}')
                print(f' \n O fatorial de {self.num2} é {self.opera.fatorial(self.num2)}')

            elif self.opcao == 19:
                self.coletar()
                print(f'\n {self.opera.fibonacci(self.num1)}')
                print(f'\n {self.opera.fibonacci(self.num2)}')

            elif self.opcao == 20:
                num1 = int(input('Informe um número: '))
                print(f'\nA soma dos dígitos de {self.num1} é: {self.opera.digitos(num1)}')

            elif self.opcao == 21:
                self.coletar()
                print(f' \n{self.opera.imprimirtodos(self.num1)}')
                print(f' \n{self.opera.imprimirtodos(self.num2)}')

            elif self.opcao == 22:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.imprimirprimos(num1)}')

            elif self.opcao == 23:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.somatodos2(num1)}')

            elif self.opcao == 24:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.collatz(num1)}')

            elif self.opcao == 25:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.perfeito(num1)}')

            else:
                return "Número inválido"







