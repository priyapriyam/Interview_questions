numbers=[0,2,3,0,4,6,0,7,10]
i=0
while i < len(numbers):
    if numbers[i]==0:
        b=numbers.pop(i)
        numbers.append(b)
    i=i+1
print numbers
    
    

