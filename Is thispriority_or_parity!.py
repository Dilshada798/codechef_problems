for i in range(int(input())):
    n,x=map(int,input().split())
    if x==1:
        print("EVEN" if n%2==0 else "ODD")
    elif x==2:
        print("ODD")
    else:
        print("EVEN")
