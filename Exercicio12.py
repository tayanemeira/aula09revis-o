eleitores = int(input("quantos eleitores foram: "))
votosbrancos = int(input("quantos votos foram em branco: "))
nulos = int(input("quantos votos foram nulos: "))
validos = int(input("quantos votos foram validos: "))
soma = (votosbrancos/eleitores)*100
soma2 = (nulos/eleitores)*100
soma3 = (validos/eleitores)*100
print (f"tivemos de votos brancos {votosbrancos}%, de nulos {nulos}% e de validos {validos}%")