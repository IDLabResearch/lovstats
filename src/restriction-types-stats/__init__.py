"""
Original Work Copyright 2012 Jan Demter <jan@demter.de>
Modified Work Copyright 2018 Ghent University - imec, Sven Lieber

This file is part of LODStats.

LODStats is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

LODStats is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with LODStats.  If not, see <http://www.gnu.org/licenses/>.
"""

# import stats modules "from xx import xx"
from A1FunctionalProperties import A1FunctionalProperties
from A4Subsumption import A4Subsumption
from A13PropertyDomains import A13PropertyDomains
from A14PropertyRanges import A14PropertyRanges
from A20LiteralPatternMatching import A20LiteralPatternMatching
from A23UniversalQuantifications import A23UniversalQuantifications
from A69DisjointProperties import A69DisjointProperties
from A70DisjointClasses import A70DisjointClasses



all_stats = [A1FunctionalProperties, A4Subsumption, A13PropertyDomains, A20LiteralPatternMatching, A14PropertyRanges, A23UniversalQuantifications, A69DisjointProperties, A70DisjointClasses]

# will hold the objects doing the stats, initialized in init_stats()
stats_to_do = []
results = {}
# init stats-objects, only do void by default
def init_stats(stats_list=all_stats):
    #stats_to_do = []
    """init classes from all available stats"""
    for stat_class in stats_list:
        stats_to_do.append(stat_class(results))
    return results

# gather data
def run_stats(s, p, o, s_blank, o_l, o_blank, statement):
    """submit one triple to objects calculating stats"""
    for stat_object in stats_to_do:
        stat_object.count(s, p, o, s_blank, o_l, o_blank, statement)

def run_stats_sparql(endpoint):
    from SPARQLWrapper import SPARQLWrapper

    sparql = SPARQLWrapper(endpoint)

    for stat_object in stats_to_do:
        stat_object.sparql(sparql)

def postproc():
    for stat_object in stats_to_do:
        stat_object.postproc()
