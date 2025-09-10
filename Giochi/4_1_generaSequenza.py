import os
import sys

while True:
    try:
        os.system("clear")
        print("----------------------------------------------------------")
        print("Ora dovrai inserire i parametri e il seme della sequenza")
        print("----------------------------------------------------------\n")
        a = int(input("inserisci a\n> "))
        c = int(input("inserisci c\n> "))
        m = int(input("inserisci m\n> "))
        print("")
        seed = int(input("inserisci il seme\n> "))
        
        x = seed

        os.system("clear")
        print(f"Sequenza (a={a}, c={c}, m={m}, x_0={x}):\n{x}, ", end="")
        while (a*x + c) % m != seed:
            x = (a*x + c) % m
            print(x, end=", ")
        
        x = (a*x + c) % m

        print(x)

        choose = input("\n\nvuoi generare una nuova sequeza [Y/n]  \n> ")

        if choose == "Y" or choose == "y":
            continue
        
        break
    except:
        continue