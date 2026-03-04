sal = float(input('Digite seu salário: '))
if sal <= 1200:
    print(f'O seu salário teve um aumento de 15% e agora está em {sal + sal * 0.15}')
else:
    print(f'O seu salário teve um auemneto de 10% e agora está em {sal + sal * 0.10}')