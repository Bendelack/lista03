x,y = map(float,input().split())

if x == 0 and y == 0:
    print('Origem')
elif x == 0 and y != 0:
    print('Eixo x')
elif y == 0 and x != 0:
    print('Eixo y')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')