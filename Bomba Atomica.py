import time

lancamento = str(input('Aperte G para lançar a bomba: '))

if lancamento == 'G':
    print("EXPLOSÃO EM:")
for c in range(10,-1,-1):
    print(c)
    time.sleep(1)

print()
print("BOOOM")
time.sleep(1)
print('Você destruiu uma cidade com várias famílias felizes.')
time.sleep(2)
print('...')
time.sleep(3)
print('Está feliz?')