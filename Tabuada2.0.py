import random
from time import sleep
print('Bem-vindo ao meu sistema de tabuada!')

resp = 'S' and 's'
continua = resp

while continua == resp:

    operacao = input("Digite / para dividir ou x para multiplicar (digite back para voltar): ")
    match operacao:
        case "/":

            def tabuadadivis (numero):
                for i in range(1, 11):
                    quociente = numero / i

                    print('{} / {} = {:.2f}'.format(numero,i,quociente))

            try:
                numero = int(input("Tabuada de divisão do número: "))
                tabuadadivis(numero)
            except ValueError:
                print("ERRO: Digite apenas números!")

            continua = input('Quer continuar? [S/N] ')



        case "x":
            def tabuadamulti (numero):
                for i in range(1, 11):
                    quociente = numero * i
                    print(f"{numero} x {i} = {quociente}")


            try:
                numero = int(input("Tabuada de multiplicação do número: "))
                tabuadamulti(numero)
            except ValueError:
                print("ERRO: Digite apenas números!")

            continua = input('Quer continuar? [S/N] ')

