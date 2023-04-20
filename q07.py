a = int(input())
b = int(input())

if a > b and a % b == 0:
    print('Multiplos')
elif b > a and b % a == 0:
    print('Multiplos')
elif a == b:
    print('Multiplos')
else:
    print('Nao multiplos')