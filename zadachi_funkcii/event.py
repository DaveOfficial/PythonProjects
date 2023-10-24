all = list([3,2,5,6])
even = list()
odd = list()

for num in all:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)