# Registering a Brain Atlas

## Use case

### Description

This specification describes the process of register a brain atlas. The process starts with a subject collection which
are imaged and processed to generate 3 derived entities: a template image data, a parcellation image data, as well as
brain parcellation labels. The first 2 entities are further transformed into volumetric representation, from which an
atlas spatial reference system is derived. The parcellation labels are converted into ontology. The final template
volume, parcellation volume, parcellation ontology as well as the atlas spatial reference system are used to form an
atlas release.

### Supported Data Queries

From a specific version of a brain atlas:

* Get the brain parcellation dataset
* Get the brain parcellation labels dataset
* Get the image stack datasets
* Get the coordinate system of the atlas spatial reference system


## Data Provenance pattern

![Registering a brain atlas](../../../assets/provtemplates/atlas-registration-prov-template.svg)


## Schemas

### Entities

The different entity types involved are described below.

| Type  | Description|
| ------------- | ------------- |
| [SubjectCollection](https://bbp.epfl.ch/schemas/neuroshapes/class-subjectcollection.html)  |     A collection of subject to be used in the experiment  |
| [TemplateImageData](https://bbp.epfl.ch/schemas/neuroshapes/class-templateimagedata.html)  |  Template image data acquired and processed from the subject collection  |
| [ParcellationImageData](https://bbp.epfl.ch/schemas/neuroshapes/class-parcellationimagedata.html)  |  Parcellation image data generated from the template image data  |
| [ParcellationLabel](https://bbp.epfl.ch/schemas/neuroshapes/class-parcellationlabel.html)  |  Parcellation labels correspond to the annotations in the parcellation image  |
| [TemplateVolume](https://bbp.epfl.ch/schemas/neuroshapes/class-templatevolume.html)  |  Template volume generated from the template image data  |
| [ParcellationVolume](https://bbp.epfl.ch/schemas/neuroshapes/class-parcellationvolume.html)  |  Parcellation volume generated from the parcellation image data  |
| [ParcellationOntology](https://bbp.epfl.ch/schemas/neuroshapes/class-parcellationontology.html)  |  Parcellation ontology converted from the parcellation label  |
| [AtlasSpatialReferenceSystem](https://bbp.epfl.ch/schemas/neuroshapes/class-atlasspatialreferencesystem.html)  |  The spatial coordinate system of the atlas space  |
| [AtlasRelease](https://bbp.epfl.ch/schemas/neuroshapes/class-atlasrelease.html)  | An atlas release comprises template volume, parcellation volume, parcellation ontology as well as the atlas spatial reference system  |
| [Protocol](https://bbp.epfl.ch/schemas/neuroshapes/class-experimentalprotocol.html)                          |     Protocol that describes the method used in the design and execution of the experiment      |


### Activities

| Type  | Description|
| ------------- | ------------- |
| [Atlas Construction](https://bbp.epfl.ch/schemas/neuroshapes/class-atlasconstruction.html)   |  Process to construct a brain atlas  |
| [Template Reconstruction](https://bbp.epfl.ch/schemas/neuroshapes/class-templatereconstruction.html)   |  Reconstruct the template image data into volumetric representation  |
| [Parcellation Reconstruction](https://bbp.epfl.ch/schemas/neuroshapes/class-parcellationreconstruction.html)   |  Reconstruct the parcellation image data into volumetric representation  |
| [Ontology Conversion](https://bbp.epfl.ch/schemas/neuroshapes/class-ontologyconversion.html)   |  Convert the parcellation label into ontological representation  |

### Agents

| Type  | Description|
| ------------- | ------------- |
| [Person](https://bbp.epfl.ch/schemas/neuroshapes/class-schemaperson.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](https://bbp.epfl.ch/schemas/neuroshapes/class-provsoftwareagent.html)                          |    Software associated with an activity      |
| [Organization](https://bbp.epfl.ch/schemas/neuroshapes/class-schemaorganization.html)                            |    Organization associated with an activity      |


## Contributors

* [Huanxiang Lu](mailto:huanxiang.lu@epfl.ch)
* [Anna-Kristin Kaufmann](mailto:anna-kristin.kaufmann@epfl.ch)
* [Silvia Jimenez](mailto:silvia.jimenez@epfl.ch)
* [Sy Mohameth Francois](mailto:mohameth.sy@epfl.ch)
* [Samuel Kerrien](mailto:samuel.kerrien@epfl.ch)
* [Sean Hill](mailto:sean.hill@epfl.ch)