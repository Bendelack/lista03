d = int(input())
a,l,p = map(int,input().split())

if d > a or d > l or d > p:
    print('N')
else:
    print('S')