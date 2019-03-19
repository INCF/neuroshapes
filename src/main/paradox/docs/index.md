
@@@ index

* [Getting Started](gettingstarted/index.md)
* [Modeling Your Data](datamodeling/index.md)
* [SHACL In a Nutshell](shacl-tutorial/overview/index.md)
* [Data Models and Formats](data-models/index.md)
* [Meetings and Workshops](meetings.md)
* [License](license.md)
* [Contact](contact.md)
* [Release Notes](releases.md)

@@@

#Neuroshapes

##Why Neuroshapes ?

The goal of Neuroshapes is the development of open, use case driven and shared validatable data models (schemas, vocabularies) to enable the FAIR principles (Findable, Accessible, Interoperable and Reusable) for basic, computational and clinical neuroscience (meta)data. The data models developed thus far entities for electrophysiology, neuron morphology, brain atlases, in vitro electrophysiology and computational modeling. Future developments could include brain imaging, transcriptomic and clinical form data, as determined by community interests.

@@@ note 

All data models presented in this documentation are still drafts.
Potential changes can be discussed on [Github](https://github.com/BlueBrain/nexus-bbp-domains) or on [Gitter](https://gitter.im/BlueBrain/nexus-schemas)

@@@


##Neuroshapes Goals

* the use of standard semantic markups and linked data principles as ways to structure metadata and related data: the W3C RDF format is leveraged, specifically its developer-friendly JSON-LD serialization. The adoption of linked data principles and JSON-LD will ease federated access and discoverability of distributed neuroscience (meta)data over the web.

* the use of the W3C SHACL (Shapes Constraint Language) recommendation as a rich metadata schema language which is formal and expressive; interoperable; machine-readable; and domain-agnostic. With SHACL, (meta)data quality can be enforced based on schemas and vocabularies (easily discoverable and searchable) rather than being fully encoded in procedural codes. SHACL also provides key interoperability capabilities to ensure the evolution of standard data models and data longevity. It allows to incrementally build standard data models in terms of semantics and sophistication.

* the reuse of existing schemas and semantic markups (like schema.org ) and existing ontologies and controlled vocabularies (including NIFSTD - NIF Standard Ontologies)

* the use of the W3C PROV-O recommendation as a format to record (meta)data provenance: a SHACL version of the W3C PROV-O is created.

## Get involved

* Join the [INCF Special Interest Group on Neuroshapes](https://www.incf.org/activities/standards-and-best-practices/incf-special-interest-groups/incf-sig-on-neuroshapes-open)
* Read the [How to contribute](./gettingstarted/contribution.html) section
