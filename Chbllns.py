
t=int(input())
for i in range (t):
    arr=list(map(int,input().split()))
    k=int(input())
    count=0
    for j in arr:
        if(j>k-1):
            count+=k-1
        else:
            count+=j

    print(count+1)
