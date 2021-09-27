import unittest

tree = {
        "node1": {
                    "node11": {
                                "node111": [1, 2, 3],
                                "node112": [31, 5]
                              },
                    "node12": [31]
                },
        "node2": [7, 8, 9]
    }
flat_tree = [1, 2, 3]

list_result = list()

def get_key_by_index(dictionary_item, index):
    var = dictionary_item.keys()
    return list(var)[index]

def remove_current_item_dictionary(item_tree):
    key_for_removing = get_key_by_index(item_tree,0)
    del item_tree[key_for_removing]
    return item_tree

def recursion(item):
   if isinstance(item, list):
       print(item)
       return item

   tree_values = item.values()   
   
   try: 
    for values in tree_values:
       if not isinstance(values,list):
           values.update(remove_current_item_dictionary(item))
           recursion(values)
       else:
           key = get_key_by_index(item, 0)
           [list_result.append(list_item) for list_item in values]
    print(list_result)
   except:
    return list_result

expected_result_tree = [1, 2, 3, 31, 5, 31, 7, 8, 9]
assert recursion(tree) == expected_result_tree,"incorrect tree plot"
assert recursion(flat_tree) == flat_tree,"incorrect tree plot"