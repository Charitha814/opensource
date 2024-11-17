n = int(input())
arr = list(map(int, input().split()))
br = arr[::-1]
res = " ".join(map(str, br))
print(res)
