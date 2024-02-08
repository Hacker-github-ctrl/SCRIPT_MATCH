#!/usr/bin/env python3
import os
import time

yellow = '\33[93m'
neutro = '\33[0m'

def opcoes_main():
    print(neutro, "Tabuada da matemática básica")
    print()
    print(yellow, "[1] adição ")
    print(yellow, "[2] subtração ")
    print(yellow, "[3] multiplicação ")
    print(yellow, "[4] divisão ")
    
    try:
        opção = int(input(neutro + "Digite uma opção: "))
        if opção == 1 or opção == 2 or opção == 3 or opção == 4:
            print(f"Então vc escolheu a opção {opção}")
            time.sleep(3)
        else:
            print("Essa opção não existe !")
    except:
        print("Digite apenas números nesse exato momento por enquanto ! ")
    
    if opção == 1:
        print("Vc escolheu a adição, então vc apenas Digita um número,")
        print("e depois... vc Digita um outro números apenas, e somar os dois !")
        print("boa sorte ;) ")
        print()
        time.sleep(17)
    
        x = int(input("Digite um número: "))
        y = int(input("Digita um outro número: "))
        if x and y != "":
            print("\nResultado: ", x + y)
            exit()
        else:
            print("Digite certo aí kct...")
    elif opção == 2:
        print("Vc escolheu a subtração, então vc apenas Digite um número,")
        print("e depois... vc Digita um outro número apenas, e subtrair os dois !")
        print("boa sorte ;) ")
        time.sleep(3)
    
        a = int(input("Digite um número: "))
        e = int(input("Digite um outro número: "))
        if a and e != "":
            print("\nResultado: ", a - e)
            exit()
        else:
            print("Já falei pra Digitar certo !")
    
    elif opção == 3:
        print("Vc escolheu a multiplicação, então vc apenas Digite um número,")
        print("e depois... Vc Digita um outro número apenas, e multiplicar os dois !")
        print("boa sorte ;)")
        print()
        
        w = int(input("Digite um número: "))
        c = int(input("Digite um outro número: "))
        if w and c != "":
            print("\nResultado: ", w * c)
            exit()
        else:
            print("Digite certo poha !")
            
    elif opção == 4:
        print("Vc escolheu a subtração, então vc apenas Digite um número,")
        print("e depois... Vc Digita um outro número apenas, e dividir os dois !")
        print("boa sorte ;)")
        print()
        
        b = int(input("Digite um número: "))
        d = int(input("Digite um outro número: "))
        if b and d != "":
            print("\nResultado: ", b / d)
            exit()
        else:
            print("Já falei mil vezes pra Digitar certo")
         
opcoes_main()