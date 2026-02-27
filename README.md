[![Join the chat at https://gitter.im/INCF/neuroshapes](https://badges.gitter.im/INCF/neuroshapes.svg)](https://gitter.im/INCF/neuroshapes?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/INCF/neuroshapes.svg?branch=master)](https://travis-ci.org/INCF/neuroshapes)
![GitHub release](https://img.shields.io/github/release/INCF/neuroshapes.svg)

# Welcome to Neuroshapes
The goal of Neuroshapes is the development of open, use-case-driven and shared, validatable data models (schemas and vocabularies) to enable the FAIR principles (Findable, Accessible, Interoperable, and Reusable) for basic, computational, and clinical neuroscience (meta)data.

The data models developed so far cover entities for electrophysiology, neuron morphology, brain atlases, in vitro electrophysiology, and computational modeling. Future developments could include brain imaging, transcriptomic, and clinical form data, as determined by community interests.

## Table of contents

- [Goal](#goal)  
- [Tutorials](#tutorials)  
- [Adoption](#adoption)  
- [Formats and standards](#formats-and-standards)  
- [Testing the schemas](#testing-the-schemas)  
- [Roadmap](#roadmap)  
- [License](#license)  

# Goal

The main goal is to promote:

- The use of standard semantic markups and [linked data principles](https://www.w3.org/standards/semanticweb/data) as ways to structure metadata and related data. The [W3C RDF format](https://www.w3.org/RDF/) is leveraged, specifically its developer-friendly [JSON-LD](https://json-ld.org/) serialization. Adoption of linked data principles and JSON-LD eases federated access and discoverability of distributed neuroscience (meta)data over the web.

- The use of the [W3C SHACL (Shape Constraint Language)](https://www.w3.org/TR/shacl) recommendation as a rich metadata schema language that is formal, expressive, interoperable, machine-interpretable, and domain-agnostic. With SHACL, (meta)data quality can be enforced based on schemas and vocabularies rather than being fully encoded in procedural code. SHACL also provides key interoperability capabilities to ensure the evolution of standard data models and data longevity.

- The reuse of existing schemas and semantic markups (like [schema.org](http://schema.org/)) and existing ontologies and controlled vocabularies (including [NIFSTD – NIF Standard Ontologies](https://github.com/SciCrunch/NIF-Ontology)).

- The use of the W3C PROV-O recommendation as a format to record (meta)data provenance. A SHACL version of W3C PROV-O is provided.

Neuroshapes also aims to create a community for open, use-case-driven development of data models (schemas and vocabularies), tools around them, and guidelines for FAIR neuroscience (meta)data.

# Tutorials

A set of tutorials from the [Blue Brain Nexus Forge](https://nexus-forge.readthedocs.io/en/latest/#getting-started) project are available and use the schemas defined in Neuroshapes as data models to create and validate datasets as well as register them in Blue Brain Nexus.

Try them in Binder:  
https://mybinder.org/v2/gh/BlueBrain/nexus-forge/v0.4.0?filepath=examples%2Fnotebooks%2Fgetting-started

# Adoption

The following projects have adopted Neuroshapes:

- [Blue Brain Project](https://bluebrain.epfl.ch)  
- [Human Brain Project](https://www.humanbrainproject.eu/en/)  
- [Krembil Centre for Neuroinformatics](https://www.camh.ca/en/science-and-research/institutes-and-centres/krembil-centre-for-neuroinformatics)  

# Formats and standards

All schemas in this repository conform to the [W3C SHACL recommendation](https://www.w3.org/TR/shacl) and are serialized using [JSON-LD](https://www.w3.org/TR/2014/REC-json-ld-20140116/).

## Testing the schemas

Two different tests are executed in the unit tests. The first test validates that schemas conform to the SHACL specifications. The second test uses valid and invalid data samples that are tested against the modeled shapes. These examples are placed in the `examples` directory and follow the directory structure of the shape they should be tested against.

Tests require Python > 3.6 and pytest. To run them:
python3 -m venv env
source env/bin/activate
pip install pytest pyshacl
pytest 

To test a specific set of shapes:
pytest --testdir=shapes/neurosciencegraph/datashapes/atlas

# Roadmap

- Creation of an INCF/neuroshapes Special Interest Group  
- INCF endorsement as a standard and best practice supporting FAIR neuroscience data  
- Extension of the current data model specifications  

# License

The license for all schemas and data is [CC-BY-4.0](https://github.com/INCF/neuroshapes/blob/master/LICENSE).