list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
b=[]
while i<len(list1):
    a=list1[i]
    if a not in b:
        b.append(a)
    i=i+1
print(b)


