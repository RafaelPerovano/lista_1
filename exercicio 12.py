carros = int(input("Digite o valor de carros vendidos: "))
vVendas = int(input("Digite o valor total de vendas: "))
com = float(input("Digite o valor da comissão em %: "))
salFixo = float(input("Digite o valor do salario fixo: "))
salF = salFixo + com * carros/100 + 5*vVendas/100
print("Seu salario final é igual a {}R$ ".format(salF))