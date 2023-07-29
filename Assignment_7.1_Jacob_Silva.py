# Made by Jacob Silva for class CIS 245, instructor Allen Voelcker
# This program is designed to take in and display a user's input.
class Vehicle:
    # Setting up the set_vehicle methods
    def set_vehicle_make(self, make):
        self.vehicle_make = make

    def set_vehicle_model(self, model):
        self.vehicle_model = model


# Constructing a car class to find amount of doors and display
class Car(Vehicle):

    def car_door(self, door):
        self.car_door = door

    def display_car(self):
        print("")
        print(f"The car make is {self.vehicle_make}, the model\n"
              f"is {self.vehicle_model}, and it has {self.car_door} doors.\n"
              f"It will be added to the registry at a later date.")


# Creating a truck class to ask for the length of inches of bed and display
class Truck(Vehicle):

    def truck_bed(self, bed):
        self.truck_bed = bed

    def display_truck(self):
        print("")
        print(f"The pickup make is {self.vehicle_make}, the model is {self.vehicle_model},\n"
              f"and its truck bed is {self.truck_bed} inches long.\n"
              f"It will be added to the registry at a later date.")


# Creating a definition to construct a response with the car input
def construct_c():
    input_make = input("Please input the make of the vehicle: ")
    input_model = input("Please input the model of the vehicle: ")
    count_door = input("What are the amount of doors? It could be in\n"
                       "numerical or written: ")
    parking1.car_door(count_door)
    parking1.set_vehicle_make(input_make)
    parking1.set_vehicle_model(input_model)
    parking1.display_car()


# Creating a definition to construct a response with the truck input
def construct_t():
    input_make = input("Please input the make of the vehicle: ")
    input_model = input("Please input the model of the vehicle: ")
    count_bed = input("What is the length of the truck bed in inches? It\n:"
                      "could be in numerical or written: ")
    parking2.truck_bed(count_bed)
    parking2.set_vehicle_make(input_make)
    parking2.set_vehicle_model(input_model)
    parking2.display_truck()


# Beginning and allowing the program to restart if needed
while True:
    import time
    input_vehicle = input("Welcome to the garage! Proceed with this program\n"
                          "to sign up your vehicle for discounted parking.\n"
                          "What type of vehicle do you drive?\n"
                          "1. Car\n"
                          "2. Pickup truck\n"
                          "3. Quit program\n")
    parking1 = Car()
    parking2 = Truck()

    if input_vehicle == "1":
        construct_c()

    if input_vehicle == "2":
        construct_t()

    if input_vehicle == "3":
        print("Thank you. Have a nice day!")
        time.sleep(2)
        break

    print()
    repeat = input("Would you like to rerun the program?\n"
                   "Press 'y' to do so, type anything else\n"
                   "to leave the program.\n")
    if repeat == "y":
        print("")
        continue
    if repeat != "y":
        print("Thank you. Have a nice day!")
        time.sleep(2)
        break
