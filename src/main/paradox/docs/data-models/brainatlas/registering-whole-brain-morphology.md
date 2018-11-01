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
| [TemplateVolume](https://bbp-nexus.epfl.ch/staging/datamodels/concept-neurosciencegraphatlastemplatevolume.html)  |  Template volume generated from the template image data  |
| [AtlasSpatialReferenceSystem](https://bbp-nexus.epfl.ch/staging/datamodels/concept-neurosciencegraphatlasatlasspatialreferencesystem.html)  |  The spatial coordinate system of the atlas space  |
| [ImageStack](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphatlasimagestackv021shapesimagestackshape.html)                            |     Image stack obtained from the brain tissue of the subject     |
| [ReconstructedCell](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyreconstructedcellv012shapesreconstructedcellshape.html)    |     Reconstructed cell      |
| [Transform](https://bbp-nexus.epfl.ch/staging/datamodels/concept-neurosciencegraphatlastransform.html)    |     A linear or non-linear transform      |
| [Protocol](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsexperimentalprotocolv011shapesexperimentalprotocolshape.html)                          |     Protocol that describes the method used in the design and execution of the experiment      |


## Activities

| Type  | Description|
| ------------- | ------------- |
| [BrainImaging](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentbrainimagingv010shapesbrainimagingshape.html)                      |     Technique used to obtain an image stack of the brain tissue containing the cells for reconstruction      |
| [ReconstructionFromImage](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyreconstructionfromimagev010shapesreconstructionfromimageshape.html)   |     Technique used to reconstruct the stained cell     |
| [Transformation](https://bbp-nexus.epfl.ch/staging/datamodels/concept-neurosciencegraphatlastransformation.html)   |     Transform a geometric object     |

## Agents

| Type  | Description|
| ------------- | ------------- |
| [Person](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonspersonv010shapespersonshape.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcoresoftwareagentv010shapessoftwareagentshape.html)                          |    Software associated with an activity      |
| [Organization](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsorganizationv010shapesorganizationshape.html)                            |    Organization associated with an activity      |


## Contributors

Huanxiang Lu <huanxiang.lu@epfl.ch>
Anna-Kristin Kaufmann <anna-kristin.kaufmann@epfl.ch>
Sy Mohameth Francois <mohameth.sy@epfl.ch>
Sean Hill <sean.hill@epfl.ch>
