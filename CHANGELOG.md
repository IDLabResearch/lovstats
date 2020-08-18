# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2020-08-18

### Added

- Several detectors for SHACL core constraints (directories `shape-constraints-stats` and `shape_constraint_detectors`)
- Detector for OWL exact qualified cardinality `owl:qualifiedCardinality`
- Detectors for OWL object and datatype domain/range (note they are not part of official OWL-RDF as it will just be `rdfs:domain` and `rdfs:range`)
- Detector for OWL subsumption `owl:subClassOf` (note this is not official OWL-RDF as it should just be `rdfs:subClassOf`)
- new commandline option to specify a repository URI where the input was taken from, which will be added as dimension to the output stats

### Changed

- Statistics namespace now `https://w3id.org/montolo/ns/montolo#` instead of `https://w3id.org/lovcube/ns/relovstats#`
- Statistics vocabulary namespace now `https://w3id.org/montolo/ns/montolo-voc#` instead of `https://w3id.org/lovcube/ns/lovcube#`

## [0.1.0] - 2018-12-10

### Added

- v0.1.0 which contains an initial version covering the detection of common RDFS and OWL axioms

[0.1.0]: https://github.com/IDLabResearch/lovstats/releases/tag/v0.1.0
[0.2.0]: https://github.com/IDLabResearch/lovstats/compare/v0.1.0...v0.2.0
