#Carly Grubbs, July 7th, M03 Lab - Case Study: Lists, Functions, and Classes
#This program will ask for information about your vehicle and then display the information

#creating a super class called Vehicle with an attribute of type
class Vehicle():
    def __init__(self, type):
        self.type = type

#Creating a child class called Automobile
#This class will gather information from the super class and setup other attributes
class Automobile(Vehicle):
    #This method will setup the attributes
    def __init__(self, type, year, make, model, doors, roof):
        Vehicle.__init__(self, type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    #This method will return the information entered from the user about their car
    def __str__(self):
        return "Vehicle type: " + self.type + "\nYear: " + self.year + "\nMake: " + self.make + "\nModel: " + self.model + "\nNumber of doors: " + self.doors + "\nType of roof: " + self.roof
        
#This method will ask the user for the information about their car, set the information equal to the attributes in automobile, and then diplay the details according to the return
def main():
    print("Please enter the following information about the vehicle:")
    year = input("Year: ")
    make = input ("Make: ")
    model = input("Model: ")
    doors = input("Number Of Doors(2 or 4): ")
    roof = input("Type Of Roof(solid or sun roof): ")
    car = Automobile("car", year, make, model, doors, roof)
    print("\nHere are the details about your car:")
    print(car)

if __name__ == "__main__":
    main()