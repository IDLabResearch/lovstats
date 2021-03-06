# LOVStats

[![DOI](https://zenodo.org/badge/161209581.svg)](https://zenodo.org/badge/latestdoi/161209581)

A LODStats extension to compute restriction type statistics for RDF data models, currently with modules for axioms (OWL, RDFS) and constraints (SHACL).
Whereas the actual extension consists of own statistical modules (`src/restriction-types-stats`, `src/shape-constraints-stats`)
and a different commandline script (`src/lodstats.py`) compared to the original LODStats.

Example, calling the `lodstats.sh` script to execute lodstats within a docker container 

```
# calling lodstats
bash lodstats.sh

# execute our statistics (if folder input mounted to docker container)
bash lodstats.sh -o restriction-types-stats /input/foaf.nt 

# execute our statistics on an HTTP uri
bash lodstats.sh -o restriction-types-stats http://xmlns.com/foaf/spec/index.rdf
```

please note that lodstats is called in the container, thus needed directories needs to be mounted in the docker-compose file or docker run command.
In the shown example, the input is taken from the mounted input directory which is mounted in the docker-compose file.

# How does LODStats work?

* LODStats is a tool implemented by AKSW Leipzig, in python 2.7.
* The tool parses input RDF and handles it as a stream.
* Multiple stats modules exist (provided in the stats folder), and the commandline script `LODStats/build/scripts-2.7/lodstats` calls the LODStats library with provided stats modules.
* For each triple the provided stats modules are executed.
* A stats module follows a specific interface (`LODStats/lodstats/stats/RDFStatInterface.py`), thus new stats modules can inherit from that interface.
* The `count` function is called for each triple, and information can be stored in own data structures.
* The `postproc` function is called when the RDF stream ends, own aggregations can then be performed on self-defined data structures.

# How does our extension work?

* We adapted the lodstats script, to take also another stats directory into account (`./src/lodstats.py` with `-o` option).
* Our stats modules for axioms are in the `restriction-types-stats` directory (including `__init__.py`, which makes the stats modules available
* Our stats modules for constraints are in the `shape-constraints-stats` directory (including `__init__.py`, which makes the stats modules available

# How to install LODStats?

```
# Create a docker image to execute LODStats with our extension
docker-compose build lodstats-execute

# Run the script
docker-compose run lodstats-execute /LODStats/scripts/lodstats
```

# How to run tests?

```
# Create a docker image to run tests
docker-compose build lodstats-test

# Execute the tests (Does currently not work)
docker-compose up lodstats-test
```
