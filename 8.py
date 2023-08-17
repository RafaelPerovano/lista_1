s0 = 2
v0 = 3
a = 10
t = float(input("Digite o valor do tempo em segundos: "))
s = s0 + v0*t + a/2 * (t*t)
print("Seu espaço percorrido é {}m".format(s))