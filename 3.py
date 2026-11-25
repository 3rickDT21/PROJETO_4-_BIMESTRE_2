print("CONTADOR DE BASES NITROGENADAS\n")
resp=input("DIGITE UMA SEQUÊNCIA DE BASES NITROGENADAS: [MAX 10]")

quanC=0
quanG=0
quanA=0
quanT=0

porcA=0
porcT=0
porcG=0
porcC=0

for letra in resp:
        if letra == "A":
            quanA+=1
            porcA+=10
        elif letra == "T":
            quanT+=1
            porcT+=10
        elif letra == "G":
            quanG+=1
            porcG+=10
        elif letra == "C":
            quanC+=1
            porcC+=10

print(f"A: {porcA}% ({quanA}/10)")
print(f"T: {porcT}% ({quanT}/10)")
print(f"C: {porcC}% ({quanC}/10)")
print(f"G: {porcG}% ({quanG}/10)")
