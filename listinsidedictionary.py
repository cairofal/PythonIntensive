#Armazenamento de lista dentro de um dicionario

pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']: print("\t" + topping) 


#Um dicionario dentro de outro

users = { 'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
         'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', },
        }

for username, user_info in users.items(): 
    print("\nUsername: " + username) 
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())