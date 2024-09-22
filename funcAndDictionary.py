#Function tha returns a dictionary with information from a person

def build_person(first_name,last_name):
    person ={'first':first_name,'last':last_name}
    return person

#Example
musician = build_person('Jimi','Hendrix')
print(musician)