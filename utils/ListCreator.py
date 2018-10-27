import utils
from pprint import pprint
class ListCreator():
    """
    This class creates a list from rdf:first, rdf:rest linked lists.
    """
    def __init__(self, predicate):
        self.listPredicate = predicate
        self.roots = {}
        self.list_values = {}
        self.list_nodes = {}
        self.list_roots = []
        self.result_lists = {}
        self.result_lists_values = {}

    def count(self, s, p, o, statement):
        # Keep track of datatypes with restrictions
        if p == self.listPredicate:
            print("in the owl if")
            print("s is: " + s)
            print("o is: " + o)
            if o in self.roots:
                self.roots[o].append(s)
            else:
                self.roots[o] = [s]
            self.list_roots.append(o)

        # Keep track of all rdf:first statements
        if p == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#first':
            # The subject is the list node, the object a list entry
            self.list_values[s] = o;

        # Keep track of all rdf:rest statements
        if p == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#rest' and \
            o != 'http://www.w3.org/1999/02/22-rdf-syntax-ns#nil':
            # The subject is the list node, the object another list node
            self.list_nodes[s] = o

    def compute(self):
        print "compute"
        print("notes")
        pprint(self.list_nodes)
        print("roots")
        pprint(self.roots)
        print("list roots")
        pprint(self.list_roots)
        print("list values")
        pprint(self.list_values)
        self.result_lists = utils.create_list_from_linked_list(self.list_nodes, self.list_roots)
        print("result lists")
        pprint(self.result_lists)
        self.result_lists_values = utils.get_list_values(self.result_lists, self.list_values, self.roots)

    def get_list(self):
        return self.result_lists_values

    def one_list_contains(self, entry):
        for listID in self.result_lists_values:
            if entry in self.result_lists_values[listID]:
                return True
        return False