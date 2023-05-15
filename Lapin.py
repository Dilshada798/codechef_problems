
for i in range(int(input())):
    s=input()
    str1=list(s[:len(s)//2])
    s=s[::-1]
    str2= list(s[:len(s)//2])
    str1.sort()
    str2.sort()
    if str1==str2:
        print("YES")
    else:
        print("NO")


