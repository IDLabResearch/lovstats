from lodstats.stats.RDFStatInterface import RDFStatInterface
from pprint import pprint

class C1Subsumption(RDFStatInterface):
    """Multiple statistics regarding Subsumption,
    - Amount of subclasses
    - Amount of class hierarchies
    - hierarchy depth for each hierarchy
    - average class hierarchy depth
    - median class hierarchy depth"""

    def __init__(self, results):
        super(C1Subsumption, self).__init__(results)
        self.graph = self.results['graph'] = {}
        self.c = self.results['count'] = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/2000/01/rdf-schema#subClassOf':
            self.graph[s] = o

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        final_depth = 0
        all_depths = [];
        for root_object, root_subject in self.results['graph'].iteritems():
            depth = 0
            objects_encountered = []
            new_depth = self.get_depth(root_subject, self.results['graph'], depth, objects_encountered)
            if (new_depth > final_depth):
                all_depths.append(final_depth)
                final_depth = new_depth
        self.c = self.results['count'] = final_depth

    def get_depth(self, root_subject, graph, depth, objects_encountered):
        """
            TODO: recursive! check if it scales
        """
        new_depth = depth
        for object, subject in graph.iteritems():
            if (object == root_subject):
                new_depth += 1
                objects_encountered.append(object)
                new_depth = self.get_depth(subject, graph, new_depth, objects_encountered)
                break
            if (new_depth > len(graph)):
                return 0
        return new_depth
