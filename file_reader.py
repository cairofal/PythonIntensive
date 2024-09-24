filename = 'pi_digitts.txt'

#The keyword with closes the file after it is not necessary anymore
with open(filename) as file_object: 
    for line in file_object:
        print(line)