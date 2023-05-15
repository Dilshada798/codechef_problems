
t = int(input())
for i in range (t): 
    n=int(input())
    x=str(input())
    y="aeiou"
    z=0
    for i in x:
        if i not in y:
            z+=1
        else :
            z=0
        if z==4:
            break
    if z==4:
        print("NO")
    else:
        print("yes")
            break
