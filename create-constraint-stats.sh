
if [ $# -ne 1 ];
then
  echo "please provide a n-triples file"
  exit 1
fi
output_dir=test-constraint-output
input_dir=test-constraint-input

args="-f nq -o shape-constraints-stats -b https://w3id.org/montolo/ns/montolo#ad-hoc -r /output/test-stats.ttl -u http://example.org/ns/test /input/schema-shacl.nt"

docker run \
-v "$(pwd)/src/RDFStats.py:/usr/local/lib/python2.7/dist-packages/lodstats-0.4.0-py2.7.egg/lodstats/RDFStats.py" \
-v "$(pwd)/src/interfaces.py:/usr/local/lib/python2.7/dist-packages/lodstats-0.4.0-py2.7.egg/lodstats/util/interfaces.py" \
-v "$(pwd)/src/:/src" \
-v "$(pwd)/src/lodstats.py:/LODStats/scripts/lodstats" \
-v "$(pwd)/$input_dir:/input" \
-v "$(pwd)/$output_dir:/output" \
lodstats-execute /LODStats/scripts/lodstats $args
# -it lodstats-execute /bin/bash

