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

## Schemas

### Entities

The different entity types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
[Subject](https://bbp.epfl.ch/schemas/neuroshapes/class-subject.html)                            |     Subject that was used in the experiment     |
| [Slice](https://bbp.epfl.ch/schemas/neuroshapes/class-slice.html)                                |     Brain slice obtained from the subject      |
| [PatchedSlice](https://bbp.epfl.ch/schemas/neuroshapes/class-patchedslice.html)                  |     Brain slice containing patched cells      |
| [PatchedCellCollection](https://bbp.epfl.ch/schemas/neuroshapes/class-patchedcellcollection.html)|     Collection of patched cells in a single slice (e.g. for multi-patch recordings) |
| [PatchedCell](https://bbp.epfl.ch/schemas/neuroshapes/class-patchedcell.html)                    |     Cell that was patched in the slice      |
| [FixedStainedSlice](https://bbp.epfl.ch/schemas/neuroshapes/class-fixedstainedslice.html)    |     Brain slice after fixation and staining     |
| [AnnotatedSlice](https://bbp.epfl.ch/schemas/neuroshapes/class-annotatedslice.html)    |    Brain slice containing the identified and annotated stained cells      |
| [LabeledCellCollection](https://bbp.epfl.ch/schemas/neuroshapes/class-labeledcellcollection.html)    |     Collection of labeled cells in a single slice     |
| [LabeledCell](https://bbp.epfl.ch/schemas/neuroshapes/class-labeledcell.html)    |     Cell that was labeled in the slice     |
| [ReconstructedCell](https://bbp.epfl.ch/schemas/neuroshapes/class-reconstructedcell.html)    |     Reconstructed cell      |
| [Protocol](https://bbp.epfl.ch/schemas/neuroshapes/class-experimentalprotocol.html)                          |     Protocol that describes the method used in the design and execution of the experiment      |

### Activities

The different activity types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [BrainSlicing](https://bbp.epfl.ch/schemas/neuroshapes/class-brainslicing.html)                      |     Technique used to obtain a brain slice for patching      |
| [WholeCellPatchClamp](https://bbp.epfl.ch/schemas/neuroshapes/class-wholecellpatchclamp.html)        |     Technique used to study electrical activity of individual living cells    |
| [FixationStainingMounting](https://bbp.epfl.ch/schemas/neuroshapes/class-fixationstainingmounting.html)    |     Technique used to fix and stain the slice      |
| [AcquisitionAnnotation](https://bbp.epfl.ch/schemas/neuroshapes/class-acquisitionannotation.html)    |     Technique used to acquire an image of the slice and annotate the stained cells     |
| [Reconstruction](https://bbp.epfl.ch/schemas/neuroshapes/class-reconstruction.html)   |     Technique used to reconstruct the stained cell     |


### Agents

The different agent types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [Person](https://bbp.epfl.ch/schemas/neuroshapes/class-schemaperson.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](https://bbp.epfl.ch/schemas/neuroshapes/class-provsoftwareagent.html)                          |    Software associated with an activity      |
| [Organization](https://bbp.epfl.ch/schemas/neuroshapes/class-schemaorganization.html)                            |    Organization associated with an activity      |

## Contributors

* [Anna-Kristin Kaufmann](mailto:anna-kristin.kaufmann@epfl.ch)
* [Huanxiang Lu](mailto:huanxiang.lu@epfl.ch)
* [Silvia Jimenez](mailto:silvia.jimenez@epfl.ch)
* [Rodrigo Perin](mailto:rodrigo.perin@epfl.ch)
* [Sy Mohameth Francois](mailto:mohameth.sy@epfl.ch)
* [Samuel Kerrien](mailto:samuel.kerrien@epfl.ch)
* [Sean Hill](mailto:sean.hill@epfl.ch)
