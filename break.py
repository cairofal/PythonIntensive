prompt = "\n Please enter the name of a city you have visited:" 
prompt += "|n Entre 'quit' when you are finished"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("\m I'd love to go to" + city.title() + "!")

