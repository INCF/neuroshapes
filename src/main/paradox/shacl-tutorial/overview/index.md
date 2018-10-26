
# SHACL In a Nutshell

This document presents an example-driven overview of the W3C SHACL recommendation for RDF data validation.

@@@ note
 The overview only introduces the W3C SHACL specification in the context of its usage within Neuroshapes. 
 For an in-depth description, the user should read the [W3C SHACL recommendation](https://www.w3.org/TR/shacl/) but also the excellent 
 set of learning resources available at the [Validating RDF website](http://www.validatingrdf.com/).
@@@




It is highly recommended to read the following section before continuing to read this document:

* [JSON for Linking Data]()

## What is SHACL ?

The **SHA**pes **C**onstraint **L**anguage (**SHACL**) is a W3C recommendation allowing to validate a RDF graph against a set of constraints defined in so-called shapes.



## JSON-LD serialization

All examples (both shapes and data) in this document are serialized using the [JSON-LD]() format unlike the [W3C SHACL recommendation](https://www.w3.org/TR/shacl/) document where [TURTLE](https://www.w3.org/TR/turtle/) is preferred.
While Turtle is more compact, JSON-LD is more suitable for exchange in the context of the web through already popular json APIs which is an important aspect for adoption purpose specially by developers.
Nevertheless, it is possible to convert from one format to the other using many converters available online. [EASYRDF](http://www.easyrdf.org/converter) is one example. 




## Namespaces and Context

JSON-LD can be very verbose if a context is not provided. To improve readability and to simplify both shapes and data examples, a SHACL context as well a prefix mappings was created as shown below.
This context is only related to the SHACL vocabulary (i.e. the set of terms defined in the SHACL specification) and **it is highly recommended** to use it.
Since writing a SHACL shape almost always required using a domain vocabulary, the SHACL context can be updated with domain specific prefix mappings or aliases when needed.
In all cases, the context below will be refer to http://example.org/shaclcontext from now on.

Prefix mappings
: @@snip [standard prefix mappings](../../assets/contexts/nexus/core/shacl20170720/prefixmapings.md)

SHACL JSON-LD context
: @@snip [shacl context](../../assets/contexts/nexus/core/shacl20170720/v0.1.0.json)
