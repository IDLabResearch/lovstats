
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