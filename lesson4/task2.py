my_list = [4, 13, 8, 42, 15, 16, 23, 66]
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(new_list)