n = map(int,input().split())
a = sum(n)
average = a / len(n)
if average>=4:
    print('Perfect')
elif average >= 3:
    print ('Good')
else:
    print('Poor')