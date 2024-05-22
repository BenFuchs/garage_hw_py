from enum import Enum
from icecream import ic
import json
class Options(Enum):
    ADD = 1
    DELETE = 2
    UPDATE = 3
    DISPLAY = 4
    INFO = 5
    RESET = 6
    EXIT = 7

def load_info():
    try:
        with open('carInfo.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def saveInfo(carInfo):
        with open('carInfo.json', 'w') as file:
            return json.dump(carInfo, file)

carInfo = load_info()


def menu():
    global user_input
    for option in Options:
        print(f'{option.name} - {option.value}')
    user_input = int(input("Please select an option: "))


def add():
    new_car_color = input("Please input car's color: ")
    new_car_name = input("Please input car owner's name: ")
    new_car_year = input("Please input car's year: ")
    new_car_brand = input("Please input car's brand: ")
    carInfo.append({"Color": new_car_color, "Owner": new_car_name, "Year": new_car_year, "Brand": new_car_brand})

def delete():
    display()
    car_del = int(input("Please choose which car you'd like to delete --> ID number: "))
    carInfo.pop(car_del)
    print("Chosen car has been deleted")

def update_info():
    display()
    car_upd = int(input("Please choose which car you'd like to update --> ID number: "))
    carInfo[car_upd] = {'Color': input("Please enter new color: "), 'Owner': input("Please enter new Owner name: "), 'Year': input("Please enter new Year: "), 'Brand': input("Please enter new brand: ")}

def display():
    for index, car in enumerate(carInfo):
        print(f'({index}) - {car["Color"]} - {car["Owner"]} - {car["Year"]} - {car["Brand"]}')

def info():
    num_of_cars = len(carInfo)
    print(num_of_cars)

def reset():
    with open('carInfo.json', 'w') as file:
        json.dump({}, file)
    carInfo.clear()
    saveInfo(carInfo)




if __name__ == "__main__":
    while True:
        menu()
        if user_input == 1: add()
        if user_input == 2: delete()
        if user_input == 3: update_info()
        if user_input == 4: display()
        if user_input == 5: info()
        if user_input == 6: reset()
        if user_input == 7: 
            saveInfo(carInfo)
            exit()
