#Displays the ingredients list 

def make_pizza(size, *toppings): # Positonal and arbitrary arguments
    print("\nMaking a " + str(size) + " cm pizza with the following toppings:") 
    for topping in toppings: print("- " + topping)
    
make_pizza(16,'pepperoni') 
make_pizza(25, 'mushrooms', 'green peppers', 'extra cheese')