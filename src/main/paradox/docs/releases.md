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


### Vocabulary, taxonomy and ontology changes

Neuroshapes main approach has been to build on top of existing initiatives for common (http://schema.org) and provenance (https://www.w3.org/TR/prov-o/) vocabularies.
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
* nsg:Entity => prov:Entity
* nsg:Activity => prov:Activity
* nsg:SoftwareAgent => prov:SoftwareAgent
* nsg:Organization => schema:Organization
* nsg:Person => schema:Person
* nsg:Collection => prov:Collection
* nsg:Collection => nsg:SubjectCollection
* nsg:Collection => prov:Collection
* nsg:EmptyCollection => prov:EmptyCollection

The above mapping brings unicity in term of types (e.g. no more nsg:Activity and prov:Activity).

Two new namespaces are introduced:

* `https://neuroshapes.org/` with `nsg` as prefix: for all neuroscience specific types, properties and shapes.
* `https://provshapes.org/`  with prov as prefix: for all W3C PROV-0 provenance related types, properties and shapes.

A [core ontology](https://github.com/INCF/neuroshapes/tree/master/ontologies) is now introduced. It contains a set of types along with their definitions.
The neurosciencegraph core data and schema contexts are also removed to avoid having users to manage them with multiple versions.
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
* BrainLocation shape

Removed:

* mediatype schema
* https://neuroshapes.org/dash/agent schema
* https://provshapes.org/dash/activity schema
* https://provshapes.org/dash/person
* https://provshapes.org/dash/organization
* https://provshapes.org/dash/entity schema
* https://provshapes.org/dash/collection
* Reused usage shape in activity shape

Constraints:

* WholeCellPatchClamp activity now used nsg:SliceCollection instead of nsg:Slice
* WholeCellPatchClamp activity now is not required to have one generated entity


### Technical and Repository structure changes

Previously, Neuroshapes' github repository was made of multiple scala modules with one module for each neuroscience domain: Neuron Morphology, Brain Atlas, Ephys recording,...
A set of shapes representing neuroscience entities were defined in each module.
The Neuroshapes scala modules themselves imported provenance shapes from [BlueBrain/nexus-prov](https://github.com/BlueBrain/nexus-prov) and some BlueBrain Nexus built-in shapes.
This structure was complex and was not easy to understand and relate with the main goals of Neuroshapes.

The `v1.0.x` release comes with a single scala module and a new simplified Github structure clearly showing:

* the recommended taxonomies: in `taxonomies` dir
* the recommended ontologies: in `ontologies` dir
* the defined shapes for provenance description and for neuroscience entities and data types: in `shapes` dir. The `shapes` dir contains two categories of shapes:
** the provenance ones in `shapes/prov`: which are now located in the Neuroshapes Github repository instead of being inherited from [BlueBrain/nexus-prov](https://github.com/BlueBrain/nexus-prov).
** the neuroscience ones: in `shapes/neurosciencegraph`

Shapes are now grouped in two categories:

* common shapes: these are libraries of useful shapes built mainly for reuse (e.g. QuantitativeValue). They often don't define a target thus preventing them from being used alone to validate data.
The related namespaces are:

** `https://neuroshapes.org/commons/`
** `https://provshapes.org/commons/`

* data shapes (`https://neuroshapes.org/dash/`): these shapes to be used to validate actual data. They often make use of common shapes and define a target.
The related namespaces are:

** `https://neuroshapes.org/dash/`
** `https://provshapes.org/dash/`
