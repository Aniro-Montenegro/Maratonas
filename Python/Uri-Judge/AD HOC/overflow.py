n = int(input())
dados = input().split(" ")
a = int(dados[0])
b = int(dados[2])
sinal = dados[1]
calculo = 0
if sinal == "*":
    calculo = a * b
if sinal == "+":
    calculo = a + b


if calculo <= n:
    print("OK")
else:
    print("OVERFLOW")
