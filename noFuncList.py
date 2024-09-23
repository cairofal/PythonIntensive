unprinted_designs = ['iphone case', 'robot pendant','dodecahedron']
completed_models = []

# Simulate the print from each design
while unprinted_designs: current_design = unprinted_designs.pop()

# Simulate the creation of a 3D print 
print("Printing model: " + current_design)
completed_models.append(current_design)

# Display all the models finished 
print("\nThe following models have been printed:") 
for completed_model in completed_models:
 print(completed_model)