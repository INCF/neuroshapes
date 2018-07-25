# Introduction

This document gathers best practices for lightweight ontology and taxonomy design and edition. 
It should be considered as a collection of guidelines to follow when contributing to Neuroshapes ontologies and taxonomies. 
Note that below I'll used ontology in general to refer to both ontologies and taxonomies.

## Namespaces
The following table shows the set of prefix names and their corresponding namespaces used this document.


## Best practices on lightweight ontology and taxonomy edition

### Documentation best practices

#### Topic and provenance
An ontology should be annotated with its purpose as well as its provenance.  The authorative vocabulary for doing this is the dublin core one.
Its official prefix name is **dc** and the corresponding namespace is **<http://purl.org/dc/elements/1.1/>**.
The following annotation should be provided: 
* dc:title
* dc:creator and/or dc:contributor
* dc:subject
 
#### Versioning

owl:versionInfo is used to provide version information. Its value should match semantic versioning pattern. 
For example "0.1.0" is valid value for owl:versionInfo but not "version_1".
 

### Entity naming

An ontology as well as entities it defines (called here ontology terms) have a [URI](https://www.w3.org/TR/uri-clarification) as identifier.
For example "http://purl.obolibrary.org/obo/NCBITaxon_10090" is the URI of a "Mus musculus" term. 
The previous URI can have a short form which is called prefix (a stable string) for the ontology and [CURIE](https://www.w3.org/TR/curie) for the ontology entities. 
Let take again the previous example. The prefix name of (the short form of) "http://purl.obolibrary.org/obo/NCBITaxon_10090" can be "obo" and resulting in a curie of the form "obo:NCBITaxon_10090". 
Given the curie "obo:NCBITaxon_10090", "obo" is the prefix name and "NCBITaxon_10090" the fragment.

How to write a good CURIE:

 - Do not use underscore preferably (for example **activ**:0000001 instead of **HBP_ACT**:0000001). 
 - A lowercase prefix name should be preferred: "activ" instead of "ACTIV"
 - Use words rather than numbers as fragment (ex. **activ:activity** instead of **activ:0000001**) if the number of ontology entities is small. 

#### Ontology term name as single noun
A term name refers to its curie's fragment. 

- Use [camel case](https://en.wikipedia.org/wiki/Camel_case) notation:
    * concept name should start with a capital letter
    * no space is allowed
    * Good example **"damo:ChannelDistribution"**
    * Bad examples  **"damo:channelDistribution"** or **"damo:channel_Distribution"**


#### Ontology term Annotations: minimal fields
 
Here are some annotation properties that can be attached to a concept to describe it.
 
 * rdfs:label: a short label that can be used to name the concept. At least a label in english should be provided (using @en as language tag). Note that only one label per language is allowed.
 * skos:prefLabel: a preferred label for an ontology term. The rdfs:label value can be reused here. Note that a skos:prefLabel is a rdfs:label.
 * Link each term with the ontology which defines it through a rdfs:isDefinedBy assertion
 
 #### Ontology property name as verb sense
 
A property name refers to its curie's fragment. 
 
- Use verb as property name so that a triple (a statement: (term, property, term)) can be easily read.
    * for example: "file:aSpecificFile **prop:hasFileExtension** ext:csv" instead of "file:aSpecificFile **prop:fileExtension** ext:csv"
- Use mixed case notation:
    * property name should start with lower case and be capitalized thereafter
    * no space is allowed
    * Good example **"prop:hasFileExtension"**
    * Bad example  **"HBP_PROP:has_file_extension"**
- Link each property with the ontology which defines it through a rdfs:isDefinedBy assertion



 ### Use of authorative vocabulary
 
 Authorative vocabulary list:
 
  * skos: http://www.w3.org/2004/02/skos/core#
  * dc:	http://purl.org/dc/elements/1.1/
  
### Frequent errors

 * rdfs:isDefinedBy is not for providing a textual definition for a term or a property but for indicating a resource within which the concept or the property is defined.