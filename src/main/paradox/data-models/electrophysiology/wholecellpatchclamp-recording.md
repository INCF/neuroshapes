# In Vitro Whole Cell Patch Clamp Recording

## Use case

### Description

This specification describes the metadata collected for in vitro intracellular electrophysiology recordings using the whole-cell patch-clamp configuration. Metadata is collected on the subject used in the experiment, the slice, the patched cell which was recorded as well as the recording traces and protocols. Additionally, metadata for the brain slicing, the whole-cell patch-clamp and the stimulus used to generate traces are captured.

### Supported Data Queries

The following points describe a subset of questions the provenance pattern above can support:
 
* Retrieve all electrophysiology traces generated from rat somatosensory cortex using selected stimuli
* Retrieve electrophysiology traces by recording day
* For a given stimulus / sweep / repetition, get a specific voltage and/or current trace.
* Get the liquid junction potential for an individual trace.


## Data Provenance pattern

![Whole-cell patch-clamp-recording](../../assets/provtemplates/wholecellpatchclamp-recording-prov-template.svg)


## Entities

The different entity types involved are described below.

| Type  | Description|
| -------------                                                             | ------------- |
| [Subject](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcoresubjectv010shapessubjectshape.html)                            |     Specimen that was used for the experimental analysis      |
| [Slice](https://bbp-nexus.epfl.ch/staging/datamodels/class-nsgslice.html)                                |     Brain slice obtained from the specimen      |
| [PatchedSlice](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentpatchedslicev011shapespatchedsliceshape.html)                  |     Brain slice with patched cells      |
| [PatchedCellCollection](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentpatchedcellcollectionv010shapespatchedcellcollectionshape.html)|     Collection of patched cells in a single slice |
| [PatchedCell](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentpatchedcellv021shapespatchedcellshape.html)                    |     Cell that was patched in the slice      |
| [Trace](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphelectrophysiologytracev100shapestraceshape.html)                         |     Individual recording trace of the patched cell (StimulationTrace and ResponseTrace)     |
| [Protocol](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsexperimentalprotocolv011shapesexperimentalprotocolshape.html)                          |     Document that describes the method used in the design and implementation of an experiment      |
    
## Activities

The different type of activities involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [BrainSlicing](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentbrainslicingv100shapesbrainslicingshape.html)                      |     Technique used to obtain a slice of brain tissue for patching      |
| [WholeCellPatchClamp](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphexperimentwholecellpatchclampv010shapeswholecellpatchclampshape.html)        |     Technique used to study ionic currents of individual living cells    |
| [StimulusExperiment](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphelectrophysiologystimulusexperimentv100shapesstimulusexperimentshape.html)   |     Technique used to obtain the electrical signature of cells through injection of a defined current patternuio |

## Agents

The different agent types involved are described below.

| Type  | Description|
| ------------- | ------------- |
| [Person](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonspersonv010shapespersonshape.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcoresoftwareagentv010shapessoftwareagentshape.html)                          |    Software associated with an activity      |
| [Organization](https://bbp-nexus.epfl.ch/staging/datamodels/shape-neurosciencegraphcommonsorganizationv010shapesorganizationshape.html)                            |    Organization associated with an activity      |

## Contributors
