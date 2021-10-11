'''
Data Scientist: Eddy Giusepe Chirinos Isidro

Este script está baseado no seguinte vídeo: https://www.youtube.com/watch?v=jtVYx9W0dgc
'''

print("##########################################")
print("Criamos um loop no python com for, assim: ")
print("##########################################")

for index in range(1, 5, 1):
    print(index)

print("################################################")
print("Criamos um loop no python com uma lista, assim: ")
print("################################################")

list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

# for number in list_test:
#     print(number)


# Também:    

for index, number in enumerate(list_test):
    print(f"INDEX: {index}")
    print(f"NUMBER: {number}")
    print("")



print("##############################")
print("Criamos um dicionário, assim: ")
print("##############################")    

obj_test = {
    "nome" : "Eddy",
    "Idade" : 40,
    "GitHub" : "EddyGiusepe",
    "Profissão" : "Data Scientist"
}

print("")

for obj in obj_test:
    print(obj)

print("")
print("Podemos também pegar os Valores desse Dicionário, assim: ")

for obj in obj_test.values():
    print(obj)

print("")
print("Podemos printar a CHAVE e o VALOR, assim: ")

for key, value in obj_test.items():
    print(f"KEY: {key}")
    print(f"VALUE: {value}")
    print("")


print("#####################")
print("Usando WHILE, assim: ")
print("#####################")      

numero = 0
while numero < 20:
    print(numero)
    numero += 1