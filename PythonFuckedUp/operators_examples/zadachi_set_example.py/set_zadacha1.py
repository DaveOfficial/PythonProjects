import random 
set1 = set()
set2 = set()
for elem in range(6):
    set1.add(random.randint(10,20))
    set2.add(random.randint(15,25))
    
print(set1) 
print(set2)

set3 = set1 & set2
print('\n This is the joint set' + str(set3))

set1 = set1 - set3

print("\n From set1 are removed the common elements:" +str(set1))