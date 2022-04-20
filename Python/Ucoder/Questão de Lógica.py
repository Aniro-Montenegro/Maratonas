
def calcularFibonacci(sequencia :int):

    if sequencia==1 or sequencia==2:
        return 1
    else:
        n=1
        a=0
        for c in range(2,sequencia):
            a=n
            n=n+a
            print(n)



n=4


calcularFibonacci(n)
