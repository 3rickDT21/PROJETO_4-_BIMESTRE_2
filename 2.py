print("BASES NITROGENADAS NO RNA\n")
resp=input("DIGITE UMA SEQUÊNCIA DE BASES NITROGENADAS:")
codigo =""

for letra in resp:        
        if letra == "A":
            codigo = codigo +"U"
        elif letra == "U":
            codigo = codigo +"A"
        elif letra == "C":
            codigo = codigo +"G"
        elif letra == "G":
            codigo = codigo +"C"
        else:
            print("SEQUENCIA INVALIDA, DIGITE OUTRAS BASES NITROGENADAS\n")
            codigo ="" 
            break
if codigo !="":
    print(codigo)