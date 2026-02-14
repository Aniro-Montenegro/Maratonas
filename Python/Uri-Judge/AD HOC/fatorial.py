def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


n = int(input())
quantidade = 0
referencial = 1
while n >= 1:
    x = fatorial(referencial)
    if x > n:
        z = fatorial(referencial - 1)
        n = n - z
        quantidade += 1
        referencial = 1
    else:
        referencial += 1

print(quantidade)
