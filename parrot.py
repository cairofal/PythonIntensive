#prompt = "\nTell me something, and I will repeat it back to you"
#prompt += "\nEnter 'quit' to end the program. \n"
#message = ""
#while message != 'quit': message = input(prompt) 
#if message != 'quit': print(message, "\n")


#Same code but using a flag 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True 
while active: message = input(prompt)
if message == 'quit': active = False 
else: print(message)