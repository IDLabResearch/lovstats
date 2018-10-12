
Repo setup according to https://www.airpair.com/docker/posts/efficiant-development-workfow-using-git-submodules-and-docker-compose

Example call
```
bash lodstats.sh /input/foaf/foaf.rdf -v
```

please note that lodstats is called in the container, thus needed directories needs to be mounted in the `lodstats.sh` script.
In the shown example, the input is taken from the mounted input directory which is mounted inside the lodstats.sh script.
