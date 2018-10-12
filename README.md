
Repo setup according to https://www.airpair.com/docker/posts/efficiant-development-workfow-using-git-submodules-and-docker-compose

Example call
```
bash lodstats.sh -p /LODStats/test/resources/heb-1.rdf -v
```

please note that lodstats is called in the container, thus needed directories needs to be mounted in the `lodstats.sh` script.
In the shown example, the input is taken from the LODStats directory which was added during the creation of the docker image.
