cFabrica = float(input("Digite o valor do custo de fabrica: "))
pDis = cFabrica*28/100
imp = cFabrica*45/100
cCarro =  cFabrica + pDis + imp
print("O valor final do carro para o consumidor é de {}R$".format(cCarro))