#Keyword arguments. Argumentos nomeados.
#Name-value association to avoid confusion.

def describe_pets(animal_type="Hamster", pet_name="Harry"):
    print("\n I have a " + animal_type + " named " + pet_name)
    
describe_pets()
describe_pets(animal_type="Crocodile", pet_name="Benjamin")
