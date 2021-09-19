import math


def menu():
    while(True):
        try:
           print("Menu:")
           print("1. Calculate triangle area by base and height")
           print("2. Calculate triangle area by 2 sides and angle between them")
           print("3. Exit")
           print("Enter menu number:")
           menu_number = int(input())
        except:
            print(f"You typed a character {menu_number} which could not be converted into integer")
                
        if(menu_number ==1):
            Area = area_by_base_height()
        elif(menu_number == 2):
            Area = area_by_2sides_angle()
        elif(menu_number == 3):
            break
        print(f"Area is: {Area}")
    
    print("Goodbye!")


def area_by_base_height():
    try:
        print("Enter base and height:")
        parameters = input()
        base,height = map(int,parameters.split(' '))
    except:
        print(f"You typed a character {parameters} which could not be converted into integer")

    return 0.5 * base * height


def area_by_2sides_angle():
    try:
        print("Enter 2 sides and angle(degrees) between them:")
        parameters = input()
        side1, side2, angle = map(int, parameters.split(' '))
    except:
        print(f"You typed a character {parameters} which could not be converted into integer")
    
    return 0.5 * side1 * side2 * math.sin(math.radians(angle))


menu()