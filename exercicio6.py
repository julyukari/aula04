dentro=0
fora=0
for i in range (10):
    num = int(input("digite o numero: "))
    if num <=10 or num>=20:
        fora=fora + 1
    else:
        dentro=dentro+1
print(f"Encontrei {dentro} numeros intervalo e {fora} numeros fora do intervalo")



