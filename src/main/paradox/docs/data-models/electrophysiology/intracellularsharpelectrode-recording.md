# In Vitro IntraCellular Sharp Electrode Recording

## Use case

### Description

This specification describes the metadata collected for in vitro intracellular electrophysiology recordings using  intracellular sharp electrodes
configuration. 
Metadata is collected on the subject used in the experiment, the slice, the cell 
which was recorded as well as the recording traces and protocols. Additionally, metadata for the brain slicing, the intracellular sharp electrodes and the stimulus (including protocols and agents) involved in the generation
of the recording traces are captured.

### Supported Data Queries

The following points describe an example subset of questions supported by the data provenance pattern:
 
* Retrieve all recording traces generated from rat somatosensory cortex using selected stimuli.
* Retrieve recording traces by recording day and experimenter.
* Retrieve all response traces from a specific recorded cell.


## Data Provenance pattern

![In Vitro IntraCellular Sharp Electrode Recording](../../../assets/provtemplates/intrasharpelectrode-recording.svg)

## Schemas

### Entities

The different entity types involved in the experiment are listed below.

| Type  | Description|
| -------------                                                             | ------------- |
| [Subject](https://bbp-nexus.epfl.ch/datamodels/class-nsgsubject.html)                            |     Subject that was used in the experiment     |
| [Slice](https://bbp-nexus.epfl.ch/datamodels/class-nsgslice.html)                                |     Brain slice obtained from the subject      |
| [IntraCellularSharpElectrodeRecordedSlice](https://bbp-nexus.epfl.ch/datamodels/class-nsgintracellularsharpelectroderecordedslice.html)                  |     Brain slice containing recorded cells      |
| [IntraSharpRecordedCellCollection](https://bbp-nexus.epfl.ch/datamodels/class-nsgintracellularsharpelectroderecordedslice.html)|     Collection of recorded cells in a single slice  |
| [IntraCellularSharpElectrodeRecordedCell](https://bbp-nexus.epfl.ch/datamodels/class-nsgintracellularsharpelectroderecordedcell.html)                    |     Cell that was recorded in the slice      |
| [Trace](https://bbp-nexus.epfl.ch/datamodels/class-nsgtrace.html)                         |     Individual recording trace of the cell (stimulation/input and response/output trace)     |
| [Protocol](https://bbp-nexus.epfl.ch/datamodels/class-nsgexperimentalprotocol.html)                          |     Protocol that describes the method used in the design and execution of the experiment      |
    
### Activities

The different activity types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [BrainSlicing](https://bbp-nexus.epfl.ch/datamodels/class-nsgbrainslicing.html)                      |     Technique used to obtain a brain slice      |
| [IntraCellularSharpElectrode](https://bbp-nexus.epfl.ch/datamodels/class-nsgintracellularsharpelectrode.html)        |     Technique used to study electrical activity of individual living cells    |
| [StimulusExperiment](https://bbp-nexus.epfl.ch/datamodels/class-nsgstimulusexperiment.html)   |     Technique used to obtain the electrical signature of cells through injection of a defined current pattern |

### Agents

The different agent types involved in the experiment are listed below.

| Type  | Description|
| ------------- | ------------- |
| [Person](https://bbp-nexus.epfl.ch/datamodels/class-schemaperson.html)                                        |    Person associated with an activity      |
| [SoftwareAgent](https://bbp-nexus.epfl.ch/datamodels/class-provsoftwareagent.html)                          |    Software associated with an activity      |
| [Organization](https://bbp-nexus.epfl.ch/datamodels/class-schemaorganization.html)                            |    Organization associated with an activity      |

## Contributors

* [Andrew Davison](mailto:andrew.davison@unic.cnrs-gif.fr)
* [Anna-Kristin Kaufmann](mailto:anna-kristin.kaufmann@epfl.ch)
* [Huanxiang Lu](mailto:huanxiang.lu@epfl.ch)
* [Silvia Jimenez](mailto:silvia.jimenez@epfl.ch)
* [Sy Mohameth Francois](mailto:mohameth.sy@epfl.ch)
* [Samuel Kerrien](mailto:samuel.kerrien@epfl.ch)
* [Sean Hill](mailto:sean.hill@epfl.ch)