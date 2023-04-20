cod,qtd = map(int,input().split())

if cod == 1:
    valor = qtd*4
    print(f'Total: R$ {valor:.2f}')
elif cod == 2:
    valor = qtd*4.5
    print(f'Total: R$ {valor:.2f}')
elif cod == 3:
    valor = qtd*5
    print(f'Total: R$ {valor:.2f}')
elif cod == 4:
    valor = qtd*2
    print(f'Total: R$ {valor:.2f}')
elif cod == 5:
    valor = qtd*1.5
    print(f'Total: R$ {valor:.2f}')