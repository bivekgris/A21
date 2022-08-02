li1 = ['John', 'Denise', 'David']
li2 = [10, 20, 30]

dic={}

for key in li1:
    for value in li2:
        dic[key]=value
        li2.remove(value)
        break
    
print (str(dic))