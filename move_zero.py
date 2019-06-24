numbers=[0,2,3,0,4,6,0,7,10]
count=0
while count < len(numbers):
    if numbers[count]==0:
        b=numbers.pop(count)
        numbers.append(b)
    count=count+1
print numbers
    
    

