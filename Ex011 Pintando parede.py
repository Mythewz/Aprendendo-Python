Width = float(input("Qual a largura da parede? "))
Heith = float(input("Qual a altura da parede? "))
Area = Width * Heith
Tinta = Area / 2
print("A parede de {}x{} tem uma área de {:.3f}² e precisara de {:.2f} litros de tinta".format(Width, Heith, Area, Tinta) )