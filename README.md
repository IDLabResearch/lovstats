
Repo setup according to https://www.airpair.com/docker/posts/efficiant-development-workfow-using-git-submodules-and-docker-compose

Example, calling the `lodstats.sh` script to execute lodstats within a docker container 
```
bash lodstats.sh /input/foaf/foaf.rdf -v
```

please note that lodstats is called in the container, thus needed directories needs to be mounted in the `lodstats.sh` script.
In the shown example, the input is taken from the mounted input directory which is mounted inside the lodstats.sh script.

# How does LODStats work?

* LODStats is a tool implemented by AKSW Leipzig, in python 2.7.
* The tool parses input RDF and handles it as a stream.
* Multiple stats modules exist (provided in the stats folder), and the commandline script `LODStats/build/scripts-2.7/lodstats` calls the LODStats library with provided stats modules.
* For each triple the provided stats modules are executed.
* A stats module follows a specific interface (`LODStats/lodstats/stats/RDFStatInterface.py`), thus new stats modules can inherit from that interface.
* The `count` function is called for each triple, and information can be stored in own data structures.
* The `postproc` function is called when the RDF stream ends, own aggregations can then be performed on self-defined data structures.

# How does our extension work?

* We adapted the lodstats script, to take also another stats directory into account (`my-lodstats.py` with `-o` option).
* Our stats modules are in the `constraint-type-stats` directory.

# How to install LODStats?
todo
