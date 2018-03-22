[![Join the chat at https://gitter.im/INCF/neuroshapes](https://badges.gitter.im/INCF/neuroshapes.svg)](https://gitter.im/INCF/neuroshapes?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/INCF/neuroshapes.svg?branch=master)](https://travis-ci.org/INCF/neuroshapes)
![GitHub release](https://img.shields.io/github/release/INCF/neuroshapes.svg)


# Welcome to Neuroshapes

# Formats and standards

All schemas in this repository conform to the [W3C SHACL recommendation](https://www.w3.org/TR/shacl) and are serialized using [JSON-LD](https://www.w3.org/TR/2014/REC-json-ld-20140116/). For practical reason, the defined schemas are combined in an envelop (an ontology actually) that conforms to [Nexus KG schema format](https://bbp-nexus.epfl.ch/dev/schema-documentation/documentation/shacl-schemas.html#shacl-schemas). 


# Testing the schemas

Schemas in this repository are tested using a [shacl workbench](https://github.com/BlueBrain/sbt-nexus-workbench) which is a SBT plugin that aids in the development of SHACL schemas in JSON-LD format for use in the [Nexus platform](https://github.com/BlueBrain/nexus). 
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
  
### License

The license for all schemas and data is [CC-BY-4.0](https://github.com/INCF/neuroshapes/blob/master/LICENSE).
  
# Neuroshapes Team

* [Members](https://github.com/orgs/INCF/teams/neuroshapes/members) and [Collaborations](https://github.com/INCF/neuroshapes/settings/collaboration)

# Roadmap

* Creation of an INCF/neuroshapes Special Interest Group
* INCF endorsement as a standard and best practice that support FAIR neuroscience data
* Extension of the current data model specifications
