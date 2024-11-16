x, n = map(int, input().split())
y = (n+99)//100
if(y>x):
    print(y-x)
else:
    print("0")
