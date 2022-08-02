details = {
    "name": "Danise",
    "age": 30,
    "salary": 90000,
    "location": "Adelaide"
}

details.update({'location':'city'})
del details['salary']
print(repr(details))
