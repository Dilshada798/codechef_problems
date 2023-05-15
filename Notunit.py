t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a%2!=0):
        n=b-a
        if(n>=3):
            if a%3==0:
                print(a,a+3)
            else:
                print(a+1,a+3)
        else:
            print(-1)
    else:
        n=b-a
        if(n>=2):
            print(a,a+2)
        else:
            print(-1)
