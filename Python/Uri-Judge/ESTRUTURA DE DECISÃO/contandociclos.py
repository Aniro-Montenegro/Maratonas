a=int(input())
i=1
while a!=-1:
    if a%2==0:
        print(f"Experiment {i}: {a//2} full cycle(s)")
        i=i+1
        a=int(input())
    else:
        a=a-1
        print(f"Experiment {i}: {a//2} full cycle(s)")
        i=i+1
        a=int(input())