unconfirmed_users = ['Mary','Bob', 'Trinity'] 
confirmed_users = []

#Check users until there's no more users to fill the list

while unconfirmed_users: 
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed: \n") 
    
    for confirmed_user in confirmed_users: 
        print(confirmed_user.title()) 

 