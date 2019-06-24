a=[0,2,3,0,4,6,0,7,10]
i=0
while i < len(a):
    if a[i]==0:
        b=a.pop(i)
        a.append(b)
    i=i+1
print a
    
    

