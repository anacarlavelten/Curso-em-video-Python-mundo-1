import math
maior = -math.inf
menor = math.inf
contador = 0
for i in range(3):
    contador =+ 1
    num = float(input(f'Digite o {contador} número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O menor número foi {menor}')
print(f'O maior número foi {maior}')
