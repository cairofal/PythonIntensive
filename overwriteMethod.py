import Car

class ElectricCar(Car): 
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #Call the __init__ method from the superclass to this subclass
        self.battery_size = 70
        
        def describe_battery(self): #Battery capacity description
            print("This car has a " + str(self.battery_size) + "-kWh battery.")
            my_byd = ElectricCar('tesla', 'model s', 2016)
            print(my_byd.get_descriptive_name()) 
            my_byd.describe_battery()
            
        def fill_gas_tank(): 
            print("This car doesn't need a gas tank")