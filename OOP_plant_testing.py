class PlantArea:
    # class attribute
    plant_active = False
    total_operation_time = 0.0
    number_of_control_panels = 3 #number of control panels which are attached to each machine
    control_panel_x_size = 25.0 #30 cm width for the panel
    control_panel_y_size = 40.0 #40 cm width for the panel
    def __init__(self, name: str, num_of_machines = 5, machine_x_size = 300.0, machine_y_size = 253.5): #creating a constractor, it's one of the magic methods
        # print(f"An area instance created: {name}") #creating unique identifier for indication where it came from with the barckets
        # run validations to the received arguments
        assert num_of_machines >= 0, f"number of machines:{num_of_machines} must be bigger than 0!" #way to check that we comply the expectations we have
        assert machine_x_size > 0.0, f"machine dimensions:{machine_x_size} must be bigger than 0.0" #passing assertion message for the test
        assert machine_y_size > 0.0, f"machine dimensions:{machine_y_size} must be bigger than 0.0"

        # assign to self object, these are instance attributes!!!
        self.name = name #now we don't need to assign name from outside, we assign it from the constractor
        self.num_of_machines = num_of_machines
        self.machine_x_size = machine_x_size
        self.machine_y_size = machine_y_size
        # when we pass a default value we also declare the variable type we want to pass
    def calculate_total_used_space(self): #we have to send at least one parameter on every method and the 
        return (self.machine_x_size/100.0) * (self.machine_y_size/100.0) * self.num_of_machines \
            + (self.control_panel_y_size/100.0) * (self.control_panel_x_size/100.0) * self.number_of_control_panels 
        # common convention is self, here is the main power of using the self we pass with it's atttributes
        
    def calculate_total_operation_time(self):
        if PlantArea.plant_active:
            PlantArea.total_operation_time += 0.01

plant_area1 = PlantArea("area1")
# plant_area1.num_of_machines = 12
# plant_area1.machine_x_size = 300.0 #in cm
# plant_area1.machine_y_size = 253.5 #in cm

plant_area2 = PlantArea("area2", 65, 500.0, 357.5)
# plant_area2.num_of_machines = 65
# plant_area2.machine_x_size = 500.0 #in cm
# plant_area2.machine_y_size = 357.5 #in cm

#even if we use constractors we can assign additional attributes outside of them

plant_area2.outside_plant = True #this attribute is not part of the constractor
# print(plant_area2.outside_plant)

# print(PlantArea.number_of_control_panels) #because this is a class attribute, we can get into it from the class itself
# print(plant_area1.number_of_control_panels) #because the instances weren't able to find the attribute from the 
# # instance level they searched for that in class level
# print(plant_area2.number_of_control_panels)

# print(PlantArea.__dict__) #print all the attributes in the class level, converting all attributes to dictionary
# print(plant_area1.__dict__) #print all the attributes in the instance level, converting all attributes to dictionary

# print(f"total used space in [m] is: {plant_area1.calculate_total_used_space()}")
plant_area1.control_panel_x_size = 20.0
plant_area1.control_panel_y_size = 50.0
plant_area1.number_of_control_panels = 12
print(f"total used space in [m] is: {plant_area1.calculate_total_used_space()}")