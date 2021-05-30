a = [1, 5, 10, 12, 16, 20]
l = [1, 2, 10, 13, 16]
i=0
c=[]
while i<len(a):
    b=a[i]
    if b  in a:
        c.append(b)
    i=i+1
print(c)
