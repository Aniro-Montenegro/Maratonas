n=int(input())
total=0
for a in range(n):
    t, v = map(int, input().split())
    total += t * v
print(total)