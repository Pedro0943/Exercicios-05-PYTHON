import time

n1 = int(input('Sequencia a partir de: '))
n2 = int(input('Progressão de: '))
calculo = n1 + (10-1) * n2

for c in range(n1,10 + calculo,n2):
    time.sleep(0.5)
    print(' {} '.format(c), end='->')

print(' ...')