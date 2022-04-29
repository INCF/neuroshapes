# In Vitro Whole Cell Patch Clamp Recording

## Use case

### Description

This specification describes the metadata collected for in vitro intracellular electrophysiology recordings using the whole cell patch clamp 
configuration. Whole cell patch clamp is a type of electrophysiological recording used to measure ionic currents over the membrane of an entire cell. 
Suction is applied to rupture the cell membrane which provides access to the intracellular space of the patched cell. 
Metadata is collected on the subject used in the experiment, the slice, the patched cell 
which was recorded as well as the recording traces 
and protocols. Additionally, metadata for the brain slicing, the whole cell patch clamp and the stimulus (including protocols and agents) involved in the generation
of the recording traces are captured.

### Supported Data Queries

The following points describe an example subset of questions supported by the data provenance pattern:
 
* Retrieve all recording traces generated from rat somatosensory cortex using selected stimuli.
* Retrieve recording traces by recording day and experimenter.
* Retrieve all response traces from a specific patched cell.
* Get the holding potential for an individual recording trace.


## Data Provenance pattern

![In Vitro Whole Cell Patch Clamp Recording](../../../assets/provtemplates/wholecellpatchclamp-recording-prov-template.svg)

## Schemas

### Entities

The different entity types involved in the experiment are listed below.

| Type  | Description|
| -------------                                                             | ------------- |
| [Subject](https://bbp.epfl.ch/schemas/neuroshapes/class-subject.html)                            |     Subject that was used in the experiment     |
| [Slice](https://bbp.epfl.ch/schemas/neuroshapes/class-slice.html)                                |     Brain slice obtained from the subject      |
| [PatchedSlice](https://bbp.epfl.ch/schemas/neuroshapes/class-patchedslice.html)                  |     Brain slice containing patched cells      |
| [PatchedCellCollection](https://bbp.epfl.ch/schemas/neuroshapes/class-patchedcellcollection.html)|     Collection of patched cells in a single slice (e.g. for multi-patch recordings) |
| [PatchedCell](https://bbp.epfl.ch/schemas/neuroshapes/class-patchedcell.html)                    |     Cell that was patched in the slice      |
| [Trace](https://bbp.epfl.ch/schemas/neuroshapes/class-trace.html)                         |     Individual recording trace of the patched cell (stimulation/input and response/output trace)     |
| [Protocol](https://bbp.epfl.ch/schemas/neuroshapes/class-experimentalprotocol.html)                          |     Protocol that describes the method used in the design and execution of the experiment      |
    
### Activities

The different activity types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [BrainSlicing](https://bbp.epfl.ch/schemas/neuroshapes/class-brainslicing.html)                      |     Technique used to obtain a brain slice for patching      |
| [WholeCellPatchClamp](https://bbp.epfl.ch/schemas/neuroshapes/class-wholecellpatchclamp.html)        |     Technique used to study electrical activity of individual living cells    |
| [StimulusExperiment](https://bbp.epfl.ch/schemas/neuroshapes/class-stimulusexperiment.html)   |     Technique used to obtain the electrical signature of cells through injection of a defined current pattern |

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