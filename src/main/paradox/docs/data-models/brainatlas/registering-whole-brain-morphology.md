# Registering a Whole Brain Morphology in an Atlas

## Use case

### Description

This specification describes the process of register a whole brain morphology into an atlas. The process starts with
reconstruction the whole brain morphologies from image stack. The image stack is used to register to the reference atlas,
resulting in a transformation. This transformation is then used to transform the reconstructed whole brain cell into the
reference atlas space.

### Supported Data Queries

* Get the whole brain morphology from a given atlas spatial reference system.
* Get the whole brain morphologies derived from a image stack


## Data Provenance pattern

![Registering a brain atlas](../../../assets/provtemplates/whole-brain-cell-transform.svg)


## Entities

The different entity types involved are described below.

| Type  | Description|
| ------------- | ------------- |
| [Subject](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcoresubjectv010shapessubjectshape.html)                            |     Subject that was used in the experiment     |
| [TemplateVolume](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphatlastemplatevolumev010shapestemplatevolumeshape.html)  |  Template volume generated from the template image data  |
| [AtlasSpatialReferenceSystem](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphatlasatlasspatialreferencesystemv010shapesatlasspatialreferencesystemshape.html)  |  The spatial coordinate system of the atlas space  |
| [ImageStack](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphatlasimagestackv020shapesimagestackshape.html)                            |     Image stack obtained from the brain tissue of the subject     |
| [ReconstructedCell](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyreconstructedcellv012shapesreconstructedcellshape.html)    |     Reconstructed cell      |
| [Transform](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphatlastransformv010shapestransformshape.html)    |     A linear or non-linear transform      |
| [Protocol](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsexperimentalprotocolv011shapesexperimentalprotocolshape.html)                          |     Protocol that describes the method used in the design and execution of the experiment      |


## Activities

| Type  | Description|
| ------------- | ------------- |
| [BrainImaging](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentbrainimagingv010shapesbrainimagingshape.html)                      |     Technique used to obtain an image stack of the brain tissue containing the cells for reconstruction      |
| [ReconstructionFromImage](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyreconstructionfromimagev010shapesreconstructionfromimageshape.html)   |     Technique used to reconstruct the stained cell     |
| [Transformation](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphatlastransformationv010shapestransformationshape.html)   |     Transform a geometric object     |

## Agents

| Type  | Description|
| ------------- | ------------- |
| [Person](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonspersonv010shapespersonshape.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcoresoftwareagentv010shapessoftwareagentshape.html)                          |    Software associated with an activity      |
| [Organization](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsorganizationv010shapesorganizationshape.html)                            |    Organization associated with an activity      |


## Contributors

* [Huanxiang Lu](mailto:huanxiang.lu@epfl.ch)
* [Anna-Kristin Kaufmann](mailto:anna-kristin.kaufmann@epfl.ch)
* [Silvia Jimenez](mailto:silvia.jimenez@epfl.ch)
* [Sy Mohameth Francois](mailto:mohameth.sy@epfl.ch)
* [Samuel Kerrien](mailto:samuel.kerrien@epfl.ch)
* [Sean Hill](mailto:sean.hill@epfl.ch)
