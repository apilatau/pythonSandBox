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


def recursion(items):
    if isinstance(items, dict):
        collector = list() 
        for value in items.values():
            collector.extend(recursion(value))
    else:
        return items
    return collector


expected_result_tree = [1, 2, 3, 31, 5, 31, 7, 8, 9]
print(recursion(tree))
print(recursion(flat_tree))
assert recursion(tree) == expected_result_tree, "incorrect tree plot"
assert recursion(flat_tree) == flat_tree, "incorrect tree plot"