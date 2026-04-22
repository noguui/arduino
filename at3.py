#laços de repetição
import time

contador = 0 
while contador < 67:
    print(contador)
    contador += 1
    time.sleep(0.01)

#atividade
n1 = int(input("coloque um numero: "))
if n1 < 1:
    while n1 < 101:
        print(n1)
        n1 += 1
        time.sleep(0.01)
else:
    print("Variavel maior que 0")