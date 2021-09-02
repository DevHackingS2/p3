import sys
import os
import time

def menu():
    print("-====| Escolha uma das opções |====-")
    print("-= [1] SEGREDO !  ")
    print("-= [2] Textinho ! ")
    print("-= [3] ??????? ")

menu()

opcoes = int(input("Digite algum número! "))

while opcoes != 0:
    if opcoes == 1:
        print(" JÁ DISSE QUE É SEGREDO, CURIOSA! ")
        break

    elif opcoes == 2:
        os.system("clear")
        message = "Está sendo desenvolvido"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        break

    elif opcoes == 3:
        break
    else:
        print("DIGITE O NUMERO MIZERA! ")
        break
    menu()
