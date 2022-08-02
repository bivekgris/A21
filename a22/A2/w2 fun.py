#calulating the min number from the list
def min_list_num(num1):
    min=num1[0]
    for n in num1:
        if n<min:
            min=n
    return min

num1=[9,2,3,5,6]
min=min_list_num(num1)
print(min)