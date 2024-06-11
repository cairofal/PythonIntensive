favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward' : 'ruby', 'phil' : 'phython'} 

for name, language in favorite_languages.items():
 print(name.title() + "'s favorite language is " + language.title() + ".")

 #Percorrer todos as chaves de um docoonário com um laço
 for name in favorite_languages.keys():
   print(name.title())

   #Ess dicionario teria a mesma saida se escrevessemos: for name in favorite_languages:

friends = ['phil', 'sarah']
for name in favorite_languages.keys(): print(name.title())
if name in friends: print(" Hi " + name.title() +
", I see your favorite language is " + favorite_languages[name].title() + "!")