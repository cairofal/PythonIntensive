def greeting(username): """"Docstrings are inside triple quotes and are used to document functions when Python is generating the documentation"""
prompt = "What's your name? "
username = input(prompt)
print("Hello " + username.title() + "!") 

greeting(username)