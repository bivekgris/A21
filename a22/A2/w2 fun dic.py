def count_adelaide(customers):
    count=0
    for customer in customers:
        if customer['postcode']>=5000 and customer['postcode']<6000:
            count+=1
    return count


customers = [{'name':'John', 'age': 52, 'postcode': 5345}, 
            {'name':'Ye', 'age': 22, 'postcode': 1234},
            {'name':'Siobhan', 'age': 67, 'postcode': 5323}]


print(count_adelaide(customers))