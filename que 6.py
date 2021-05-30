n=int(input("enter the number :"))
x=65
for i in range(1,n+1):
    j=0
    while j<=n-i:
        print("  ",end="  ")
        j=j+1
    for j in range(1,i+1):
        ch=chr(x)
        print(ch,end=" ")
        print(j,end=" ")
        x+=1
    x-=1
    print(ch,end="")
    for k in range(j-1,0,-1):
        x-=1
        ch=chr(x)
        print(k,end=" ")
        print(ch,end=" ")
    print()
    x=65