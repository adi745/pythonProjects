class PlantArea:
    def __init__(self, name): #creating a constractor, it's one of the magic methods
        print(f"An area instance created: {name}") #creating uniqe identifier for indication where it came from with the barckets

    def calculate_total_used_space(self, machine_x_size, machine_y_size, num_of_machines): #we have to send at least one parameter on every method and the 
        return (machine_x_size/100.0) * (machine_y_size/100.0) * num_of_machines
        # common convention is self
        

plant1 = PlantArea("area1")
plant1.num_of_machines = 12
plant1.machine_x_size = 300.0 #in cm
plant1.machine_y_size = 253.5 #in cm

plant2 = PlantArea("area2")
plant2.num_of_machines = 65
plant2.machine_x_size = 500.0 #in cm
plant2.machine_y_size = 357.5 #in cm

# print(type(plant1))
# print(type(plant1.area))
# print(type(plant1.num_of_machines))
# print(plant1.calculate_total_used_space(plant1.machine_x_size, plant1.machine_y_size, plant1.num_of_machines))
# print(plant2.calculate_total_used_space(plant2.machine_x_size, plant2.machine_y_size, plant2.num_of_machines))