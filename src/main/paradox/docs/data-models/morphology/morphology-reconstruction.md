# In Vitro Slice Neuron Morphology Reconstruction

## Use case

### Description

This specification describes metadata collected for morphology reconstructions from brain slices. Reconstruction of a neuron morphology from slice typically
follows the injection of a dye during a whole cell patch clamp recording. Some of the activities
and entities shown here are hence shared with the in vitro whole cell patch clamp recording. Metadata is collected on the subject used in the experiment, 
the slice containing the cell, the labeled cell and the reconstructed neuron morphology. The dye-filled neuron is most commonly visualized using a 
histological technique following the fixation of the brain tissue. The stained cells are annotated and then reconstructed.
Metadata from all these procedures is captured as well as the protocols used and the persons, software and organizations involved in each of the steps.
 
 
### Supported Data Queries

The following points describe an example subset of questions supported by the data provenance pattern:

* Retrieve morphology reconstructions from a given brain region.
* Retrieve pyramidal cell reconstructions.
* Retrieve morphology reconstructions from a specific experimenter.
* Retrieve morphology reconstructions from a subject of a given age and sex.
* Retrieve morphology reconstructions which were reconstructed in a given year


## Data Provenance pattern

![In Vitro Slice Neuron Morphology Reconstruction](../../../assets/provtemplates/morphology-reconstruction-prov-template.svg)


## Entities

The different entity types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
[Subject](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcoresubjectv010shapessubjectshape.html)                            |     Subject that was used in the experiment     |
| [Slice](https://bbp-nexus.epfl.ch/staging/datamodels/class-nsgslice.html)                                |     Brain slice obtained from the subject      |
| [PatchedSlice](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentpatchedslicev011shapespatchedsliceshape.html)                  |     Brain slice containing patched cells      |
| [PatchedCellCollection](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentpatchedcellcollectionv010shapespatchedcellcollectionshape.html)|     Collection of patched cells in a single slice (e.g. for multi-patch recordings) |
| [PatchedCell](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentpatchedcellv021shapespatchedcellshape.html)                    |     Cell that was patched in the slice      |
| [FixedStainedSlice](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyfixedstainedslicev010shapesfixedstainedsliceshape.html)    |     Brain slice after fixation and staining     |
| [AnnotatedSlice](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyannotatedslicev010shapesannotatedsliceshape.html)    |    Brain slice containing the identified and annotated stained cells      |
| [LabeledCellCollection](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologylabeledcellcollectionv010shapeslabeledcellcollectionshape.html)    |     Collection of labeled cells in a single slice     |
| [LabeledCell](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologylabeledcellv020shapeslabeledcellshape.html)    |     Cell that was labeled in the slice     |
| [ReconstructedCell](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyreconstructedcellv012shapesreconstructedcellshape.html)    |     Reconstructed cell      |
| [Protocol](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsexperimentalprotocolv011shapesexperimentalprotocolshape.html)                          |     Protocol that describes the method used in the design and execution of the experiment      |

## Activities

The different activity types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [BrainSlicing](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentbrainslicingv100shapesbrainslicingshape.html)                      |     Technique used to obtain a brain slice for patching      |
| [WholeCellPatchClamp](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentwholecellpatchclampv010shapeswholecellpatchclampshape.html)        |     Technique used to study electrical activity of individual living cells    |
| [FixationStainingMounting](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyfixationstainingmountingv100shapesfixationstainingmountingshape.html)    |     Technique used to fix and stain the slice      |
| [AcquisitionAnnotation](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyacquisitionannotationv010shapesacquisitionannotationshape.html)    |     Technique used to acquire an image of the slice and annotate the stained cells     |
| [Reconstruction](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphmorphologyreconstructionv011shapesreconstructionshape.html)   |     Technique used to reconstruct the stained cell     |


## Agents

The different agent types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [Person](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonspersonv010shapespersonshape.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcoresoftwareagentv010shapessoftwareagentshape.html)                          |    Software associated with an activity      |
| [Organization](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsorganizationv010shapesorganizationshape.html)                            |    Organization associated with an activity      |

## Contributors

* [Anna-Kristin Kaufmann](mailto:anna-kristin.kaufmann@epfl.ch)
* [Huanxiang Lu](mailto:huanxiang.lu@epfl.ch)
* [Silvia Jimenez](mailto:silvia.jimenez@epfl.ch)
* [Rodrigo Perin](mailto:rodrigo.perin@epfl.ch)
* [Sy Mohameth Francois](mohameth.sy@epfl.ch)
* [Sean Hill](sean.hill@epfl.ch)
