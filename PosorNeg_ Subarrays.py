for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = 0
    c = 0
    for j in range(n):
        if a[j]>0:
            b+ = j+1 
        else:
            c += j+1
    print(abs(b-c))
        
