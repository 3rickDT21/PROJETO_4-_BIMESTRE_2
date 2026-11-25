import periodictable

#print("CALCULADORA MOLECULAR\n")
#moleculacomp=input("Digite uma molécula\n Nota: Não é necessário utilizar o texto subscrito para a entrada das moléculas. Exemplo: H20, H2CO3, Ca3(PO4)2") 
#elemento = periodictable.elements[moleculacomp]



#print(f"Nome: {elemento.name}")
#print(f"Símbolo: {elemento.symbol}")
#print(f"Massa atômica: {elemento.mass}")
#print(f"Densidade: {elemento.density}")

print("BASES NITROGENADAS\n")
resp=input("DIGITE UMA SEQUÊNCIA DE BASES NITROGENADAS:").upper()
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


    