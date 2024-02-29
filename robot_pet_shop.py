# Amir Abu Hani
class PetRobots:
    def __init__(self, name, id, price, main_material, cost_to_fix_per_day, battery_type, animal_type):
        self.name = name
        self.id = id
        self.price = int(price)
        self.main_material = main_material
        self.cost_to_fix_per_day = int(cost_to_fix_per_day)
        self.battery_type = battery_type
        self.animal_type = animal_type

    def present_pet(self):
        return {
            "name": self.name,
            "id": self.id,
            "price": self.price,
            "main material": self.main_material,
            "cost to fix per day": self.cost_to_fix_per_day,
            "battery type": self.battery_type,
            "animal_type": self.animal_type
        }


class Employee:
    def __init__(self, name, id, batter_type, daily_salary):
        self.name = name
        self.id = id
        self.battery_type = batter_type
        self.daily_salary = int(daily_salary)


class Store:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.petsSale = []  # all the pets that available for sale is entered in this list
        self.petsRepair = []  # when the pet is broken, it entered to the petsRepair list
        self.sold = []  # when the pet is  sold, it entered to the sold list and removed from the petsSale list

    def for_sale(self, petrob):
        self.petsSale.append(petrob)
        print(f"The {petrob.name} robot is for sale. here are his details:  ")
        pet_info = petrob.present_pet()
        for key, value in pet_info.items():
            print(f"{key}: {value}")
        print()

    def broken(self, petrob):
        print(f"The {petrob.name} robot has entered into repair.")
        self.petsRepair.append(petrob)
        self.balance -= petrob.cost_to_fix_per_day

    # def present_petsRobotRepair(self):
    #     for item in self.petsRepair:
    #         pet_info = item.present_pet()
    #         for key, value in pet_info.items():
    #             print(f"{key}: {value}")
    #         print()

    def salaryEmployee(self, employ):
        self.balance -= employ.daily_salary

    def buyPetRobots(self, petrob):
        if petrob in self.petsSale:
            print(f"your {petrob.name} robot purchase has been made successfully. Thank you")
            self.sold.append(petrob)
            self.balance += petrob.price
            self.petsSale.remove(petrob)
        else:
            print(f"The {petrob.name} robot  does not exists in the store. ")

    def show_pets_by_price(self, start_price, end_price):
        found_pet = False
        for pet in self.petsSale:
            if start_price <= pet.price <= end_price:
                found_pet = True
                pet_info = pet.present_pet()
                for key, value in pet_info.items():
                    print(f"{key}: {value}")
                print()
        if not found_pet:
            print("No pets found within the specified price range.")


###########################################  App ##################################################
store = Store("pet robots store")
petrobot1 = PetRobots("dog", "1", 100, "iron", 10, "lithium", "herbivore")
petrobot2 = PetRobots("lion", "2", 350, "steel", 20, "lithium", "carnivore")
petrobot3 = PetRobots("tiger", "3", 250, "copper", 40, "alkaline", "carnivore")
petrobot4 = PetRobots("rabbit", "4", 120, "glass", 35, "lithium", "herbivore")
petrobot5 = PetRobots("cow", "5", 170, "plastics", 60, "alkaline", "herbivore")
petrobot6 = PetRobots("cheetah", "6", 190, "wood", 100, "lithium", "carnivore")
petrobot7 = PetRobots("giraffe", "7", 220, "iron", 90, "alkaline", "carnivore")
petrobot8 = PetRobots("horse", "7", 370, "steel", 110, "lithium", "herbivore")
employee1 = Employee("quantumBot", "100", "alkaline", 80)
employee2 = Employee("quantumBot", "101", "alkaline", 70)
employee3 = Employee("quantumBot", "103", "lithium", 95)

print(f"Welcome to the {store.name} ")
print("Her ara all the pet robots that available in the store: ")
print()
store.for_sale(petrobot2)
store.for_sale(petrobot4)
store.for_sale(petrobot7)
store.for_sale(petrobot8)
store.for_sale(petrobot5)
print("Here are the pet robots in repair: ")
store.broken(petrobot3)
store.broken(petrobot6)
store.broken(petrobot1)

store.salaryEmployee(employee1)
store.salaryEmployee(employee2)
store.salaryEmployee(employee3)
print()
start_price = int(input("Enter start price range for show available pets: "))
end_price = int(input("Enter end price range for show available pets: "))
store.show_pets_by_price(start_price, end_price)
while True:
    user_pet = input("choose your pet robot: lion/rabbit/giraffe/horse/cow/exit: ")
    if user_pet == "lion":
        store.buyPetRobots(petrobot2)
    elif user_pet == "rabbit":
        store.buyPetRobots(petrobot4)
    elif user_pet == "giraffe":
        store.buyPetRobots(petrobot7)
    elif user_pet == "horse":
        store.buyPetRobots(petrobot8)
    elif user_pet == "cow":
        store.buyPetRobots(petrobot5)
    elif user_pet == "exit":
        break
    else:
        print("Invalid pet robot input")

employeesCost = employee1.daily_salary + employee2.daily_salary + employee3.daily_salary
print(f"All the 3 employees cost is: {employeesCost}$")
print(f"Today, the store balance is {store.balance}$")
