details = {"fname":"John", "height":"190cm", "weight":"52kg", "age":30}
details['lname']='smith'
details["interests"] = ["programming", "reading", "cooking", "gardening"]

print(details)

#adding dictionary element
#name['Key']=value

print(details['lname'])


#accessing dictionary element
#name['key']

details.update({'lname':'Giri'})
print(details)

#update dictionary 
#name.update({'key':value})

details.pop("interests")
print(details)