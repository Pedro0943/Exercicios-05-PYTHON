import time

nfinal = int(input('Escolha o último número: '))

soma = 0
for c in range(0+1,nfinal+1,2):
    soma += c
    print(c)

print('-='*15)

print(soma)

print('-='*15)
