import unittest

def create_user(name, surname, **kwargs):
    result_dictionary = {
       "name": name,
       "surname": surname,       
    }
    age = kwargs.get("age")
    key_occupation = kwargs.get("occupation")
    key_won_nobel = kwargs.get("won_nobel")

    for arg in kwargs.values():        
        if arg == age and arg != None:
            additioanal_age = {"age" : age}       

        if arg == key_occupation and key_occupation != None:
            additioanal ={
                "occupation" : key_occupation             
            }

        if arg == key_won_nobel and key_won_nobel != None:
            additioanal.update({
                "won_nobel" : key_won_nobel             
            })
    if age != None:
        result_dictionary.update(additioanal_age)
    else:
        result_dictionary.update({"age" : 42})
    
    if key_occupation != None and key_won_nobel != None:
        extra_dict = {"extra" : additioanal }
        result_dictionary.update(extra_dict)

    return result_dictionary

print(create_user("John", "Doe"))
print(create_user("Bill", "Gates", age=65))
print(create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True))

assert create_user("John", "Doe") == {'name': 'John', 'surname': 'Doe', 'age': 42}, "invalid dictionary build"
assert create_user("Bill", "Gates", age=65) == {'name': 'Bill', 'surname': 'Gates', 'age': 65}, "invalid dictionary build"
assert create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == {'name': 'Marie', 'surname': 'Curie', 'age': 66, 'extra': {'occupation': 'physicist', 'won_nobel': True}},"invalid dictionary build" 