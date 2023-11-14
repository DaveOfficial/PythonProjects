import random
l1 = []
l2 = list()
for fuck in range(6):
    l1.append(random.randint(-50,50))
    l2.append(random.randint(-50,50))
print(l1,'---',l2)

for i in range(0,(len(l1)*2),2):
    print(i)
    l2.insert(i, (num for num in l1))
    
print(l2)

