string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
i=0
a=[]
while i<len(string_list):
    b=string_list[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)
