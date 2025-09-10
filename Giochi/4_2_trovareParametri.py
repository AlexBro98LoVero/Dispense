from math import gcd
import os


def modinv(a, m):
    """Modular inverse of a modulo m, if it exists."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None  # no inverse exists
    return x % m

def extended_gcd(a, b):
    """Extended GCD algorithm. Returns (gcd, x, y) such that ax + by = gcd"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def lcg_bruteforce(x0, x1, x2, x3, max_m=100):
    results = []

    for m in range(2, max_m + 1):
        for a in range(m):
            for c in range(m):
                if ((a*x0 + c) % m == x1 % m and
                    (a*x1 + c) % m == x2 % m and
                    (a*x2 + c) % m == x3 % m):
                    results.append((m, a, c))
    
    return results


def find_lcg_parameters(X0, X1, X2, X3 ):
    # Step 1: compute differences
    s0 = X1 - X0
    s1 = X2 - X1
    s2 = X3 - X2

    # Step 2: compute T = s2*s0 - s1^2
    T = s2 * s0 - s1**2
    T_abs = abs(T)
    divisors = [d for d in range(2, T_abs+1) if T_abs % d == 0]

    results = []
    for m in divisors:
        s0_mod = s0 % m
        s1_mod = s1 % m
        inv = modinv(s0_mod, m)
        if inv is None:
            continue
        a = (s1_mod * inv) % m
        c = (X1 - a*X0) % m

        # verify
        X1_check = (a*X0 + c) % m
        X2_check = (a*X1 + c) % m
        X3_check = (a*X2 + c) % m
        if X1_check == X1 % m and X2_check == X2 % m and X3_check == X3 % m:
            results.append((m, a, c))

    if not results:
        print("Valori non trovati tramite metodo classico. \nProva attacco brute-force (m=100)\n")
        results = lcg_bruteforce(X0, X1, X2, X3)

    return results


#5, 9, 7, 8
while True:
    try:
        os.system("clear")
        print("----------------------------------------------------------")
        print("Inserisci 4 valori contigui nella sequenza")
        print("----------------------------------------------------------\n")

        x_0 = int(input("inserisci x_0\n> "))
        x_1 = int(input("inserisci x_1\n> "))
        x_2 = int(input("inserisci x_2\n> "))
        x_3 = int(input("inserisci x_3\n> "))
        
        print("\n")

        candidates = find_lcg_parameters(x_0, x_1, x_2, x_3)
        print("Parametri validi: ")

        for m, a, c in candidates:
            print(f"m={m}, a={a}, c={c}")

        choose = input("\n\nvuoi generare una nuova sequeza [Y/n]  \n> ")

        if choose == "Y" or choose == "y":
            continue
        
        break
    except:
        continue