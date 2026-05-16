dias = int(input("Quantos dias você ficou com o carro ? "))
km = float(input("Quantos Km rodados nesse tempo ? "))
valor = dias * 60 + km * 0.15
print("Saiba que a diaria é 60R$ e cada quilometro rodado são 0.15R$ \n Sabendo disso e que você rodou {}km e ficou {} dias com o carro o valor a ser pago é {}".format(km, dias, valor))