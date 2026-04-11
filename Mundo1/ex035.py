a1 = float(input('Digite o primeiro ângulo: '))
a2 = float(input('Digite o segundo ângulo: '))
a3 = float(input('Digite o terceiro ângulo: '))
if a1 + a2 < a3 and a1 + a3 < a2 and a2 + a3 < a1:
    print('Não será possível fazer um triângulo')
else:
    print('Será possível fazer o triângulo')