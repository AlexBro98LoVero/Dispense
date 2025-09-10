import os
import sys

while True:
    #try:
        os.system("clear")
        print("----------------------------------------------------------")
        print("Ora dovrai inserire i parametri e il seme della sequenza")
        print("----------------------------------------------------------\n")
        a = int(input("inserisci a\n> "))
        c = int(input("inserisci c\n> "))
        m = int(input("inserisci m\n> "))
        print("")
        seed = int(input("inserisci il seme\n> "))
        
        values = [seed]

        os.system("clear")
        print(f"Sequenza (a={a}, c={c}, m={m}, x_0={seed}): ")

        while (a*values[-1] + c) % m not in values:
            values.append((a*values[-1] + c) % m)
        
        values.append(seed)

        for i in range(len(values)-1):
            print(values[i], end=", ")
        print(values[-1])
        

        choose = input("\n\nvuoi generare una nuova sequeza [Y/n]  \n> ")

        if choose == "Y" or choose == "y":
            continue
        
        break
    #except:
        continue