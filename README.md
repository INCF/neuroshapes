[![Join the chat at https://gitter.im/INCF/neuroshapes](https://badges.gitter.im/INCF/neuroshapes.svg)](https://gitter.im/INCF/neuroshapes?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/INCF/neuroshapes.svg?branch=master)](https://travis-ci.org/INCF/neuroshapes)
![GitHub release](https://img.shields.io/github/release/INCF/neuroshapes.svg)

# Note

This is the new simplified structure of Neuroshapes. A [v0](https://github.com/INCF/neuroshapes/tree/v0) branch is available to work with the previous schemas format.

# Welcome to Neuroshapes
The goal of Neuroshapes is the development of open, use case driven and shared validatable data models (schemas, vocabularies) to enable the FAIR principles (Findable, Accessible, Interoperable and Reusable) for basic, computational and clinical neuroscience (meta)data.
The data models developed thus far entities for electrophysiology, neuron morphology, brain atlases, in vitro electrophysiology and computational modeling.
Future developments could include brain imaging, transcriptomic and clinical form data, as determined by community interests.

Table of contents:

* [Goal](#goal)
* [Tutorials (WIP)](#tutorials)
* [Adoption](#adoption)
* [Formats and standards](#formats-and-standards)
* [License](#License)
* [Testing the schemas](#testing-the-schemas)
* [Roadmap](#roadmap)


# Goal

The main goal is to  promote:


* the use of standard semantic markups and [linked data principles](https://www.w3.org/standards/semanticweb/data) as ways to structure metadata and related data: the [W3C RDF format](https://www.w3.org/RDF/) is leveraged, specifically its developer friendly [JSON-LD](https://json-ld.org/) serialization. The adoption of linked data principles and JSON-LD will ease federated access and discoverability of distributed neuroscience (meta)data over the web.


*  the use of the [W3C SHACL (Shape Constraint Language)](https://www.w3.org/TR/shacl) recommendation as a rich metadata schema language which is formal and expressive; interoperable; machine interpretable; and domain agnostic. With SHACL, (meta)data quality can be enforced based on schemas and vocabularies (easily discoverable and searchable) rather than being fully encoded in procedural codes. SHACL also provides key interoperability capabities to ensure the evolution of standard data models and data longevity. It allows to incrementally build standard data models in term of semantics and sophistication.



*  the reuse of existing schemas and semantic markups (like [schema.org](http://schema.org/)) and existing ontologies and controlled vocabularies (including [NIFSTD - NIF Standard Ontologies](https://github.com/SciCrunch/NIF-Ontology))



*  the use of  W3C PROV-O recommendation as a format to record (meta)data provenance: a SHACL version of the W3C PROV-O is created.


Also, Neuroshapes aims at creating a community for an open and use case driven development of not only data models (schemas and vocabularies) and tools around them but also guidelines for FAIR neuroscience (meta)data.

# Tutorials

Please check out our tutorials:
 - [Nexus KG Schema Format](https://bbp-nexus.epfl.ch/staging/schema-documentation/documentation/shacl-schemas.html#nexus-kg-schemas)
 - [Jupyter notebook with basic operations using Nexus](https://github.com/BlueBrain/nexus/blob/v0/tutorial/basic_operations_nexus_v0.ipynb)


# Adoption

The following projects have adopted Neuroshapes:

* [Blue Brain Project](https://bluebrain.epfl.ch)
* [Human Brain Project](https://www.humanbrainproject.eu/en/)
* [Krembil Centre for Neuroinformatics](https://www.camh.ca/en/science-and-research/institutes-and-centres/krembil-centre-for-neuroinformatics)

# Formats and standards
All schemas in this repository conform to the [W3C SHACL recommendation](https://www.w3.org/TR/shacl) and are serialized using [JSON-LD](https://www.w3.org/TR/2014/REC-json-ld-20140116/). For practical reasons, the defined schemas are combined in an envelop (an ontology actually) that conforms to [Nexus KG schema format](https://bbp-nexus.epfl.ch/dev/schema-documentation/documentation/shacl-schemas.html#shacl-schemas).

# License
The license for all schemas and data is [CC-BY-4.0](https://github.com/INCF/neuroshapes/blob/master/LICENSE).

# Testing the schemas

## With sbt

Schemas in this repository are tested using a [shacl workbench](https://github.com/BlueBrain/sbt-nexus-workbench) which is a SBT plugin that helps in the development of SHACL schemas in JSON-LD format for use in the [Nexus platform](https://github.com/BlueBrain/nexus).
Please follow these steps to run the tests:

* [Install sbt](https://www.scala-sbt.org/1.0/docs/Setup.html)
* Clone the INCF/neuroshapes repository and run the tests

```shell
# Go to home
cd  ~

# Clone the repository
git clone https://github.com/INCF/neuroshapes.git

cd neuroshapes

# Run 'sbt'
sbt

# Run 'test'
test

  ```

## With Pytest

To test all shapes inside neuroshapes run:

    pip install pytest pyshacl
    mv ~/virtualenv/python3.6/bin/owlrl.py ~/virtualenv/python3.6/bin/owlrl
    pytest tests

To test an specific shape add a parameter --scan_dir, for example:

    pytest tests --scan_dir=../neuroshapes/shapes/neurosciencegraph/commons/list/

These tests are going to validate that schemas conforms with the SHACL specifications. And if you add examples you want the tests to validate you need to provide them inside a directory called `valid` or `invalid` as depicted next:

```
|-- shapes
|   |-- neurosciencegraph
|   |   |-- datashapes
|   |   `-- commons
|   |       `-- list
|   |           |-- schema.json
|   |           `-- examples
|   |               |-- datashapes.json 
|   |               `-- valid
|   |               |   `-- recipe_ingredients_list.json 
|   |               `-- invalid
|   |                   `-- recipe_missing_ingredients.json
|   `-- prov     
`-- ...

```

# Roadmap

* Creation of an INCF/neuroshapes Special Interest Group
* INCF endorsement as a standard and best practice that support FAIR neuroscience data
* Extension of the current data model specifications
