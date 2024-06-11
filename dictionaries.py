#A dictionary is a kind of data structure that stores items in key-value pairs

coffee = {'variety': 'Gesha', 'plantation_date' : 'February 2024'};
print(coffee['variety'])

#Adicionar novos pares chave
coffee['treatment'] = 'organic'
print(coffee)

#Criar um dicionario inicialmente vazio
coffee2 = {} 

#Deletar um dicionario
del coffee['treatment']
print(coffee)

#Modificando valores em um dicionario
alien_0 = {'color':'green'}
print("The alien is:" + alien_0['color']+".")
alien_0 = 'yellow'
print("The alien is now:" + alien_0['color']+".")



