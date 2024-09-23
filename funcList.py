#Displays a simple greeting for each member of a list

def greet_users(names):
    for name in names: 
        msg = "Hello, " + name.title() + "!"
        print(msg)
   
    usernames = ["hanna", "martha", "bob", "margot"]
    
    greet_users(usernames)