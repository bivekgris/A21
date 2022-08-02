lst1=[1,2,3,4]
lst2=[4,5,6,7]
lst3=lst1+lst2
lst4=lst1*len(lst2)
lst1.append('list1')
lst1.extend(lst2)
lst2.pop()
lst1.extend(lst2)
lst2=lst1.copy()
print(lst1.count(4))
print(lst1)
print(lst2)

#clear() function clear the list
#'+' add two list into a new list
#list.append() add item in the list
#list.extend() add another list into the list
#remove('x') remove item x from the list
#pop()  remove last item from the list

#list.sort() will sort the elements in a list in ascending order

#list.sort(reverse=True) will sort the elements in a list in descending order

#list.sort(key=str.lower)
#list.sort(key=str.upper)

#list.count('4')
