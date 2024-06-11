favorite_languages = {
'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

friends = ['phil', 'sarah']

for name in favorite_languages.keys(): print(name.title())
if name in friends: print(" Hi " + name.title() +
", I see your favorite language is " +
favorite_languages[name].title() + "! \n")


if 'erin' not in favorite_languages.keys(): 
    print("Erin, please take our poll! \n")



#Percorrendo chaves de um dicionario em ordem usando um laço

for name in sorted(favorite_languages.keys()): print(name.title() + ",thank you for taking the poll.")
print()

#Percorrendo todos os valores de um dicionario com um laço
#Essa abordagem extrai todos os valores do dicionario, sem verificar se ha repetiçoes. Para evitar repetiçoes é importante usar um conjnuto (set)

print("The following languages have been mentioned:") 
for language in favorite_languages.values(): print(language.title())


#