produto = float(input("Digite o valor do produto desejado: R$"))
desconto =  produto - (produto * 5 / 100)
print("Com um desconto de 5% aplicado ao valor de {}, o produto passará a custar {:.2f}".format(produto, desconto))
