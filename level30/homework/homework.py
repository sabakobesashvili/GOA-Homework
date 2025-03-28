def find_item(item_list, item):
    for i in range(len(item_list)):
        if item_list[i] == item:
            return True
    else:
        return False
print(find_item([3, 2, 1, 5, 6, 7], 3))

#2)

def max_list(num_list):
    maxIn_list = num_list[0]
    for i in num_list:
        if i > maxIn_list:
            maxIn_list = i
    return maxIn_list
print(max_list([1121, 13131, 1231441, 4041141, 556467, 21456, 23132, 1000123, 10011241, 10021231, 100311, 100411, 1005531, 1006571, 1007492, 10089203, 100912, 1010]))


#3)

def increment_list(num_list):
    for i in range(len(num_list)):
        num_list[i] += 1
    return num_list
print(increment_list([10, 11, 12, 13, 14]))


#4)

def reverse_string(word):
    return word[::-1]
print(reverse_string("input"))