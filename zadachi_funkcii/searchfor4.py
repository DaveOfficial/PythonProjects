def search(st,sp):
    l1 = []
    st= int(st)
    sp= int(sp)
    for x in range(st,sp+1):
        l1.append(x)
    
    for num in l1:
        if num%10 == 4:
            print(num)
            
start = input('Enter: ')
stop = input('Enter: ')
search(start,stop)