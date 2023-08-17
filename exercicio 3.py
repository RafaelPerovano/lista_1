hP = float(input("Digite o valor da altura da parede: "))
lP = float(input("Digite o valor da largura da parede: "))
hA = float(input("Digite o valor da altura da azulejo: "))
lA = float(input("Digite o valor da largura da azulejo: "))
areaP = hP * lP
areaA = hA * lA
azulejos = areaP / areaA
print("Voce precisara de {} azulejos ".format(azulejos))