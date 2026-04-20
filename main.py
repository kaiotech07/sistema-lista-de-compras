print("---------- SISTEMA DE LISTA DE COMPRA -----------")

itens = input("Digite cada item da lista separado por virgula: ")
lista = itens.split(",")

print(" ")

for index,item in enumerate(lista):
    index += 1
    print(f"{index} - {item}")

print(" ")

lista_final = ", ".join(lista)
print(f"Lista: {lista_final}")
print("--------------------------------------------------")