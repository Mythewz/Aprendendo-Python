from math import hypot
n1 = float(input("digite o valor do cateto oposto: "))
n2 = float(input("digite o valor do cateto adjacente: "))
# print("A hipotenusa vai medir {:.2f}".format(hypot(n1,n2)))

# ou

print("A hipotenusa vai medir: {:.2f}".format((n1*n1 + n2*n2) ** 0.5))