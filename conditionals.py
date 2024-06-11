cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars: 
    if car == 'bmw': print(car.upper()) 
    else: print(car.title)


#And & or to check two conditions

age_01 = 22
age_02 = 23

age_01 = 21 and age_02 >= 23 #return true

age_01 = 21 or age_02 >= 23 #return false 

#Uso da palavra reservada in para verificar se um item esta na lista
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings #True
'pepperoni' in requested_toppings #False

#Uso da palavra reservada not
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: print(user.title() + ", you can post a response if you wish")

#If-elif-else
#Teste de mais de duas situaçoes possiveis. O codigo é executado até que uma delas seja satisfeita. Quando uma condição é satisfeita, as demais são ignoradas. 
if age < 4: print("Your admission cost is $0.")  # type: ignore
elif age < 18: print("Your admission cost is $5.")  # type: ignore
else: print("Your admission cost is $10.")

