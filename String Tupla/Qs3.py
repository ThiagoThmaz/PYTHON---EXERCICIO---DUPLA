strings = []

for i in range(10):
    string = input("Digite uma string: ")
    strings.append(string)

print("As strings digitadas, em ordem inversa, são:")
for string in reversed(strings):
    print(string)
