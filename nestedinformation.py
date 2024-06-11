#Nested information

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

#for alien in aliens: 
  #  print(alien)

#Criar 30 alienigenas verdes
for alien_number in range(30): 
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)

 #Mostra os 5 primeiros alienigenas
 for alien in aliens[:5]: 
    print(alien)

#Mostra quantos alienigenas foram criados
print("Total number of aliens: " + str(len(aliens)))

#Transforma alienigenas amarelos em vermelhos
for alien in aliens[0:3]: 
   if alien['color'] == 'green': 
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
   elif alien['color'] == 'yellow': alien['color'] = 'red'
   alien['speed'] = 'fast'
   alien['points'] = 15