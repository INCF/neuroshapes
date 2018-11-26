# Introduction

This document gathers best practices for lightweight ontology and taxonomy design and edition. 
It should be considered as a collection of guidelines to follow when contributing to Neuroshapes ontologies and taxonomies. 
Note that the term 'ontology' in this document is used to refer to both ontologies as well as taxonomies.

## Namespaces
The following table shows the set of prefix names and their corresponding namespaces used in this document.


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

owl:versionInfo is used to provide version information. Its value should match the semantic versioning pattern. 
For example "0.1.0" is a valid value for owl:versionInfo whereas "version_1" is not.
 

### Entity naming

An ontology as well as entities it defines (called here ontology terms) have a [URI](https://www.w3.org/TR/uri-clarification) as identifier.
For example "http://purl.obolibrary.org/obo/NCBITaxon_10090" is the URI of the term "Mus musculus". 
The previous URI can have a short form which is called prefix (a stable string) for the ontology and a [CURIE](https://www.w3.org/TR/curie) for the ontology entities. 
Let's take the previous example again. The prefix name of (i.e. the short form of) "http://purl.obolibrary.org/obo/NCBITaxon_10090" can be "obo", resulting in a curie of the form "obo:NCBITaxon_10090". 
Given the curie "obo:NCBITaxon_10090", "obo" is the prefix name and "NCBITaxon_10090" the fragment.

How to write a good CURIE:

 - No underscores (for example **activ**:0000001 instead of **BBP_ACT**:0000001). 
 - Lower case prefix names (for example "activ" instead of "ACTIV").
 - Words instead of numbers as fragment (for example **activ:activity** instead of **activ:0000001**) if the number of ontology entities is small. 

#### Ontology term name as single noun
A term name refers to its curie's fragment. 

- Use [camel case](https://en.wikipedia.org/wiki/Camel_case) notation:
    * concept name should start with a capital letter
    * no space is allowed
    * good example **"damo:ChannelDistribution"**
    * bad examples  **"damo:channelDistribution"** or **"damo:channel_Distribution"**


#### Ontology term Annotations: minimal fields
 
Here are some annotation properties that can be attached to a concept to describe it.
 
 * rdfs:label: a short label that can be used to name the concept. At least a label in English should be provided (using @en as language tag). Note that only one label per language is allowed.
 * skos:prefLabel: a preferred label for an ontology term. The rdfs:label value can be reused here. Note that a skos:prefLabel is a rdfs:label.
 * Link each term with the ontology which defines it through a rdfs:isDefinedBy assertion.
 
 #### Ontology property name as verb sense
 
A property name refers to its curie's fragment. 
 
- Use a verb as property name so that a triple (a statement: (term, property, term)) can be easily read.
    * for example: "file:aSpecificFile **prop:hasFileExtension** ext:csv" instead of "file:aSpecificFile **prop:fileExtension** ext:csv"
- Use mixed case notation:
    * the property name should start with lower case and be capitalized thereafter
    * no space is allowed
    * good example **"prop:hasFileExtension"**
    * bad example  **"BBP_PROP:has_file_extension"**
- Link each property with the ontology which defines it through a rdfs:isDefinedBy assertion



 ### Use of authorative vocabulary
 
 Authorative vocabulary list:
 
  * skos: http://www.w3.org/2004/02/skos/core#
  * dc:	http://purl.org/dc/elements/1.1/
  
### Frequent errors

 * rdfs:isDefinedBy is not for providing a textual definition for a term or a property but for indicating a resource within which the concept or the property is defined.
