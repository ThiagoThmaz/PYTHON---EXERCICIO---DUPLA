def calcular_somas(v):

    somas = []

 
    inicio = 0
    fim = len(v) - 1
    while inicio <= fim:
        soma = v[inicio] + v[fim]
        somas.append(soma)
        inicio += 1
        fim -= 1


    return somas


n = int(input("Digite um inteiro n: "))

numeros = []
for i in range(n):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)


resultados = calcular_somas(numeros)

print("As somas são:")
for soma in resultados:
    print(soma)
