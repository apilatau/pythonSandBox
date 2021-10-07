import math


def menu():
    while True:
        print("Menu:")
        print("1. Calculate triangle area by base and height")
        print("2. Calculate triangle area by 2 sides and angle between them")
        print("3. Exit")        
        try:           
           menu_number = int(input("Enter menu number: "))
        except:
            print(f"You typed a character which could not be converted into integer")
            continue
                
        if menu_number == 1:
            area = area_by_base_height()
        elif menu_number == 2:
            area = area_by_2sides_angle()
        elif menu_number == 3:
            print("Goodbye!")
            break
        else:
            continue
        print(f"Area is: {area}")
        

def area_by_base_height():
    try:        
        parameters = input("Enter base and height: ")
        base, height = map(int, parameters.split(' '))
    except:
        print(f"You typed a character {parameters} which could not be converted into integer")
        return

    return 0.5 * base * height


def area_by_2sides_angle():
    try:
        print("Enter 2 sides and angle(degrees) between them:")
        parameters = input()
        side1, side2, angle = map(int, parameters.split(' '))
    except:
        print(f"You typed a character {parameters} which could not be converted into integer")
        return
    
    return 0.5 * side1 * side2 * math.sin(math.radians(angle))


menu()