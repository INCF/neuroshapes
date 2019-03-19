# Release Notes


## Neuroshapes 1.0.x

The main goal of Neuroshapes is to provide design patterns, best practices as well as tools to promote:

* The use of standard semantic markups and linked data principles as ways to structure metadata and related data.
* The use of the W3C SHACL (Shapes Constraint Language) recommendation as a rich metadata schema language which is formal and expressive; interoperable; machine-readable; and domain-agnostic.
* The reuse of existing schemas and semantic markups ( schema.org , W3C PROV-O ) and existing ontologies and controlled vocabularies (including NIFSTD - Neuroscience Information Framework Standard Ontologies).
* The use of the W3C PROV-O recommendation as a format to record (meta)data provenance.

In Neuroshapes, many neuroscience data types are specified based on the key scientific and technical activities and agents that lead to their generation.
The specifications are defined in validatable provenance-based data models and implemented using open and interoperable semantic web technologies.

Neuroshapes has been used in production within various [organisations](https://incf.github.io/neuroshapes/#adoption) for more than a year.

Find below the notable changes from the previous release.


### Identifiers and namespaces

Previously

### Vocabulary, taxonomy and ontology changes

Neuroshapes main approach has been to build on top of existing initiatives for common vocabulary (http://schema.org) and provenance vocabulary (https://www.w3.org/TR/prov-o/).
The `v1.0.x` release includes major alignment in terms of vocabularies with a systematic map to schema.org and W3C PROV-O if relevant and available:

* nsg:datePublished => schema:datePublished
* dcterms:hasPart => schema:hasPart
* nsg:hasPart => schema:hasPart
* dcterms:isPartOf => schema:isPartOf
* dcat:Distribution => schema:DataDownload
* nsg:endedAtTime => prov:endedAtTime
* nsg:startedAtTime => prov:startedAtTime
* schema:mediaType => schema:encodingFormat
* dcat:downloadURL => schema:contentUrl
* dcat:accessURL => schema:url
* nxv:digest => nsg:digest

A [core ontology](https://github.com/INCF/neuroshapes/tree/master/ontologies) is now introduced. It contains a set of types along their definitions.
The neurosciencegraph core data and schema context are also removed to avoid having users to manage them with multiple versions.
Instead, the two contexts will only be generated upon Neuroshapes release:

* data context: this context is identified by and accessible at https://incf.github.io/neuroshapes/contexts/data.json
* schema context: this context is identified by and accessible at https://incf.github.io/neuroshapes/contexts/schema.json

This release represents a commitment to backwards compatibility for contexts, vocabulary and ontologies in all future releases.

### Shapes changes

Added:
* contribution, license and language shapes
* taxonomy and ontology shapes
* boundingbox shape
* distribution shape

Removed
* mediatype schema

### Technical and Repository structure changes

Previously, Neuroshapes' github repository was made of multiple scala modules with one module for each neuroscience domain: Neuron Morphology, Brain Atlas, Ephys recording,...
A set of schemas representing neuroscienceentities were defined in each module.
The Neuroshapes scala modules themselves imported provenance schemas from [BlueBrain/nexus-prov](https://github.com/BlueBrain/nexus-prov) and some BlueBrain Nexus built-in schemas.
This structure was complex and was not easy to understand and relate with the main goals of Neuroshapes as well as its content.

The `v1.0.x` release comes with a single scala module and a new simplified Github structure clearly showing:

* the recommended taxonomies: in `taxonomies` dir
* the recommended ontologies: in `ontologies` dir
* the defined schemas for provenance description and for neuroscience entities and data types: in `shapes` dir. The `shapes` dir contains two categories of schemas:
** the provenance ones in `shapes/prov`: which are now located in the Neuroshapes Github repository instead of being inherited from [BlueBrain/nexus-prov](https://github.com/BlueBrain/nexus-prov).
** the neuroscience ones: in `shapes/neurosciencegraph`

Schemas are now grouped in two categories:

* common shapes: these are libraries of useful shapes built mainly for reuse (e.g. QuantitativeValue). They often don't define a target thus preventing them from being used alone to validate data.
* data shapes: these shapes to be used to validate actual data. They often make use of common shapes and define a target.
