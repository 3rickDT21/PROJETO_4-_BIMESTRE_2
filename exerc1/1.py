def exe1():
    intro=input("Escolha um número de um a cinco para ver informações ou realizar atividades sobre o DNA\n")

    if intro == "1":
        print("BASES NITROGENADAS\n")
        resp=input("DIGITE UMA SEQUÊNCIA DE BASES NITROGENADAS:")
        codigo =""

        for letra in resp:        
            if letra == "A":
                codigo = codigo +"T"
            elif letra == "T":
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

if __name__ == "__main__":
    exe1()
