# In Vitro Slice Neuron Morphology Reconstruction

## Use case

### Description

This specification describes metadata collected for in vitro morphology reconstruction using a slice. The process of obtaining a 
reconstructed cell typically begins with the injection of a dye during the electrophysiology recording. Some of the activities
and entities shown here are shared with the electrophysiology whole-cell patch-clamp recording. The metadata is collected
starting with the specimen, the slice, the patched cell. The stained neuron is most commonly visualized with a histological procedure
 following the fixation of the tissue where the cells can be identified and annotated to proceed then with the reconstruction
 of the cell. Metadata from all these procedures is captured as well as the protocols used and the persons, software and 
 organizations involved in each of the steps. The reconstructed cell has the link towards the binary file with the actual 
 morphology reconstruction.
 
 
### Supported Data Queries

* Retrieve all morphologies reconstructions
    - from brain region X.
    - in layer X and that are pyramidal cells.
    - from experimentalist X or from Lab Y.
    - that contain information about where the axon projects to.
    - a specimen under treatment x.
    - a specimen of age X, gender Z.
    - that have a 3D soma type.
    - from 2015 onwards.



## Data Provenance pattern

![Morphology reconstruction](../../assets/provtemplates/morphology-reconstruction-prov-template.svg)




## Entities

The different entity types involved are described below.

| Type  | Description|
| ------------- | ------------- |
| [Subject](../entities/experiment/subject.html)    |     Specimen that was used for the experimental analysis     |
| [Slice](../entities/experiment/slice.html)    |     Brain slice obtained from the specimen      |
| [PatchedSlice](../entities/experiment/patchedslice.html)    |    Brain slice with patched cells      |
| [PatchedCellCollection](../entities/experiment/patchedcellcollection.html)    |    Collection of patched cells in a single slice     |
| [PatchedCell](../entities/experiment/patchedcell.html)    |    Cell that was patched in the slice    |
| [FixedStainedSlice](../entities/morphology/fixedstainedslice.html)    |     Brain slice after fixation and staining     |
| [AnnotatedSlice](../entities/morphology/annotatedslice.html)    |    Brain slice containing the identified and annotated stained cells      |
| [LabeledCellCollection](../entities/morphology/labeledcellcollection.html)    |     Collection of labeled cells in a single slice     |
| [LabeledCell](../entities/morphology/labeledcell.html)    |     Cell that was labeled in the slice     |
| [ReconstructedCell](../entities/morphology/reconstructedcell.html)    |     Digitally reconstructed cell      |
| [Protocol](../entities/experiment/protocol.html)    |     Document that describes the method used in the design and implementation of an experiment     |

## Activities

| Type  | Description|
| ------------- | ------------- |
| [BrainSlicing](../entities/experiment/brainslicing.html)    |     Technique used to obtain a slice of brain tissue for patching       |
| [WholeCellPatchClamp](../entities/experiment/wholecellpatchclamp.html)    |     Technique used to study ionic currents of individual living cells      |
| [FixationStainingMounting](../entities/morphology/fixationstainingmounting.html)    |     Process of fixation and staining of the slice and mounting it on a slide      |
| [AcquisitionAnnotation](../entities/morphology/acquisitionannotation.html)    |     Process of acquiring the image of the slice and annotating the stained cells     |
| [Reconstruction](../entities/morphology/reconstruction.html)   |     Process of obtaining a reconstructed cell      |


## Agents

| Type  | Description|
| ------------- | ------------- |
| [Person](../entities/core/person.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](../entities/core/softwareagent.html)                          |    Software associated with an activity      |
| [Organization](../entities/core/organization.html)                          |    Organization associated with an activity      |

