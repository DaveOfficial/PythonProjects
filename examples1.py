import random
l = 'fickdeinetürkischemutterlehrerin '
l1 = l.upper()
s1 = list(l1)
s2=list()
s2.insert(0,3)
s2.append(4)
s2.append(11)
s2.insert(2,0)
s2.remove(11)
s2.sort()
s2[1] = 9
s2.reverse()
print(s2)
s2.extend(s1)
random.shuffle(s2)
print(s2)
print(random.choice(s2))