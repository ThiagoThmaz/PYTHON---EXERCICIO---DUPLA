import random

def numero_aleatorio_se_positivo(numero):
    if numero > 0:
        return random.randint(1, 1000)
    else:
        return "O número não é positivo."

# Exemplo de chamada da função
numero = 5
resultado = numero_aleatorio_se_positivo(numero)
print("Número aleatório:", resultado)
