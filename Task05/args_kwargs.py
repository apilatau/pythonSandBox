def create_user(name, surname, age=42, **extra):

    return {
        'name': name, 
        'surname': surname,
        'age': age,
        'extra': extra
    } 

print(create_user("John", "Doe"))
print(create_user("Bill", "Gates", age=65))
print(create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True))

assert create_user("John", "Doe") == {'name': 'John', 'surname': 'Doe', 'age': 42, 'extra':{}}, "invalid dictionary build"
assert create_user("Bill", "Gates", age=65) == {'name': 'Bill', 'surname': 'Gates', 'age': 65, 'extra':{}}, "invalid dictionary build"
assert create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == {'name': 'Marie', 'surname': 'Curie', 'age': 66, 'extra': {'occupation': 'physicist', 'won_nobel': True}},"invalid dictionary build" 