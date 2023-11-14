import random
l1 = []
l2 = list()
for sm in range(3):
    l1.append(random.randint(-50,50))
    l2.append(random.randint(-50,50))
print(l1,'---',l2)


for num in l2:
    for ind in range(-1,(len(l1)*2),2):
        if ind == -1:
            continue
        l1.insert(ind,num)
        
print(l1)