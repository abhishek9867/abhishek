a=[]
b=[]
l=int(input("enter list"))
for i in range(l):
    m=int(input("Enter value for a:"))
    n=int(input("Enter value for b:"))
    a.append(m)
    b.append(n)
print(a,b)
t=(a+b)
print(t)
for i in range(len(t)):
    for j in range(len(t)):
        if t[i]<t[j]:
            s=t[i]
            t[i]=t[j]
            t[j]=s
print(t)
