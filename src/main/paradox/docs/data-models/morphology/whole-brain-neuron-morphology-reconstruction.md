# Whole Brain Neuron Morphology Reconstruction

## Use case

### Description
 organizations involved in each of the steps. The reconstructed cell has the link towards the binary file with the actual 
 morphology reconstruction.
 
 
### Supported Data Queries

* Queries



## Data Provenance pattern

![Whole Brain Neuron Morphology Reconstruction](../../../assets/provtemplates/morphology-reconstruction-prov-template.svg)




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

