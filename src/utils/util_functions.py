from pprint import pprint

# -----------------------------------------------------------------------------
def compute_depths(graph, roots):
    """
    Computes the depths within graph for each given root
    :param graph:
    :param roots:
    :param depths:
    :return:

    >>> test_hierarchy = {"Vehicle": ["Car", "Plane", "Bike"], "Car": ["SportsCar", "FamilyCar"], \
    "SportsCar": ["FormulaCar"], "Machine": ["DrillingMachine"], "DrillingMachine": ["Bosch"], \
    "Person": ["Adult", "Child"], "Adult": ["Doctor"]}
    >>> compute_depths(test_hierarchy, ["Vehicle", "Machine", "Person"])
    [3, 2, 2]
    """
    depths = []
    for root in roots:
        if root in graph:
            depth = count_depth(graph, root, 0, 0)
            depths.append(depth)
    return depths

# -----------------------------------------------------------------------------
def count_depth(graph, node, level, depth):
    """
    Counts the deepest hierarchy in a tree given via graph. E.g. graph could look like:
    {   "Vehicle": ["Car", "Plane", "Bike"],
        "Car": ["SportsCar", "FamilyCar"],
        "SportsCar", ["FormulaCar"]
    }
    :param graph: The tree data structure, where each parent is a key, and its children are in an array as values
    :param node: The parent within the tree, for which the deepest depth should be computed
    :param level: The current level (the function calls itself recursively with changing levels)
    :param depth: The current depth (the function calls itself recursively with changing depth)
    :return: The deepest depth from the given node within graph

    >>> car_hierarchy = {"Vehicle": ["Car", "Plane", "Bike"], "Car": ["SportsCar", "FamilyCar"], "SportsCar": ["FormulaCar"]}
    >>> count_depth(car_hierarchy, "Vehicle", 0, 0)
    3
    >>> car_hierarchy = {"Vehicle": ["Car", "Plane", "Bike"], "Car": ["SportsCar", "FamilyCar"]}
    >>> count_depth(car_hierarchy, "Car", 0, 0)
    1
    """
    if node in graph:
        level += 1
        if level > depth:
            depth = level
        for child in graph[node]:
            depth = count_depth(graph, child, level, depth)
            level -+ 1
    return depth

# -----------------------------------------------------------------------------
def create_list_from_linked_list(graph, roots):
    """
    Recreate a list based on a serialized linked list
    :param graph:
    :param roots:
    :return:

    >>> linked_list = {"thirdEntry": "fourthEntry", "firstEntry": "secondEntry", "root": "firstEntry", "secondEntry": "thirdEntry"}
    >>> create_list_from_linked_list(linked_list, ["root"])
    {'root': ['firstEntry', 'secondEntry', 'thirdEntry', 'fourthEntry']}

    >>> linked_list = {"root2": "firstEntry2", "firstEntry": "secondEntry", "root": "firstEntry", "secondEntry": "thirdEntry"}
    >>> create_list_from_linked_list(linked_list, ["root", "root2"])
    {'root': ['firstEntry', 'secondEntry', 'thirdEntry'], 'root2': ['firstEntry2']}
    """
    lists = {}
    for root in roots:
        if root in graph:
            list_entries = find_childs(graph, root, [])
            lists[root] = list_entries
    return lists

# -----------------------------------------------------------------------------
def gather_results(detectors):
    """
    Execute the d.compute method for each given detector.
    After that the result (d.getDetectorOutput()) method is called and added as value
    under the key d.getName() to the result which is returned in the end.
    :param detectors:
    :return:
    """
    results = {}
    for d in detectors:
        d.compute()
        results[d.getName()] = d.getDetectorOutput()

    return results

# -----------------------------------------------------------------------------
def get_list_values(list, list_values, root_entries):
    """

    :param list:
    :param list_entries:
    :return:

    >>> my_roots = {'root': 'list1', 'root2': 'list2'}
    >>> my_list = {'root': ['firstEntry', 'secondEntry', 'thirdEntry'], 'root2': ['firstEntry2']}
    >>> my_list_values = {'firstEntry': 'firstValue', 'secondEntry': 'secondValue', 'thirdEntry': 'thirdValue', 'firstEntry2': 'firstValue2'}
    >>> get_list_values(my_list, my_list_values, my_roots)
    {'list1': ['firstValue', 'secondValue', 'thirdValue'], 'list2': ['firstValue2']}
    """
    result_lists = {}
    for list_root in list:

        current_entries = []
        # collect all the list entries
        for list_entry in list[list_root]:
            if list_entry in list_values:
                current_entries.append(list_values[list_entry])

        # Append the current entries to the result
        if list_root in root_entries:
            name_root = root_entries[list_root]
        else:
            name_root = list_root
        result_lists[name_root] = current_entries
    return result_lists

# -----------------------------------------------------------------------------
def find_childs(graph, parent, found_elements):
    """
    Recursively iterate through graph to find all list elements

    >>> linked_list = {"thirdEntry": "fourthEntry", "firstEntry": "secondEntry", "root": "firstEntry", "secondEntry": "thirdEntry"}
    >>> results = []
    >>> find_childs(linked_list, "root", results)
    ['firstEntry', 'secondEntry', 'thirdEntry', 'fourthEntry']
    """
    if parent in graph:
        found_elements.append(graph[parent])
        find_childs(graph, graph[parent], found_elements)
    return found_elements