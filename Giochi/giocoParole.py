import os
import string

def scambio(txt, a, b):
    ida = [i for i in range(len(txt)) if txt[i] == a]
    idb = [i for i in range(len(txt)) if txt[i] == b]

    for i in ida:
        txt = txt[:i] + b + txt[i+1:]
    for i in idb:
        txt = txt[:i] + a + txt[i+1:]
    
    return txt


def gioco():
    txt = """hder tivo ser ripo sa uovo, ufe gorpe i vezzopaotno, lti sde uilene non anlettolle
sa vonla, ldllo i cena e i porba, i ceuonsi serro cmotpete e ser taenltite sa hderra,
gaen, hdica i dn ltillo, i tacltanpetca, e i mtenset uotco e bapdti sa badve, lti dn
mtovonlotao i seclti, e dn’ivmai uoclaeti sirr’irlti mitle; e ar monle, ufe aga uonpadnpe
re sde tage, mit ufe tensi inuot mas cencaqare irr’ouufao hdecli lticbotvizaone, e cepna
ar mdnlo an uda ar ripo uecci, e r’issi tanuovanuai, met tamaprait moa nove sa ripo soge
re tage, irronlininsoca sa ndogo, ricuain r’iuhdi saclensetca e tirrenlitca an ndoga
porba e an ndoga cena."""


    while(True):
        os.system("clear")
        print("----------------------------------------------------------------------------------------")
        print(txt)
        print("----------------------------------------------------------------------------------------")
        print("")
        print("[+] che lettere vuoi scambiare ? (formato: a b)")
        letters = input("> ").strip().split(" ")
        
        if len(letters) != 2:
            continue

        a, b = letters

        a = a.lower()
        b = b.lower()

        if len(a) != 1 or len(b) != 1:
            continue

        if a not in string.ascii_lowercase or b not in string.ascii_lowercase:
            continue


        txt = scambio(txt, a, b)
        


gioco()