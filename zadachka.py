import random

l1 = list()
evenNum = list()
oddNum = list() 
for x in range(7):
    l1.append(int(input('Enter: ')))

print(l1)

for num in l1:
    if num%2==0:
        evenNum.append(num)
    else:
        oddNum.append(num)
        
print(evenNum)
print(oddNum)

randlist = list()

for i in range(5):
    randlist.append(random.randrange(0,10.0,2))
    
print(randlist)