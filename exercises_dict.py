user_input = list(input('Type down\n'))
my_dict = {i:user_input.count(i) for i in user_input}
print(my_dict)