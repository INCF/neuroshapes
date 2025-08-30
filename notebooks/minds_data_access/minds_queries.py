"""
SPARQL queries for accessing MINDS data from EBRAINS Knowledge Graph
"""

# Basic MINDS dataset discovery
FIND_MINDS_DATASETS = """
PREFIX openminds: <https://openminds.ebrains.eu/vocab/>
PREFIX schema: <https://schema.org/>
PREFIX kg: <https://kg.ebrains.eu/api/instances/>

SELECT DISTINCT ?dataset ?name ?description ?authors
WHERE {
    ?dataset a openminds:Dataset ;
             schema:name ?name ;
             schema:description ?description .
    
    OPTIONAL {
        ?dataset schema:author ?authors .
    }
    
    FILTER(
        CONTAINS(LCASE(?description), "minds") ||
        CONTAINS(LCASE(?name), "minds") ||
        CONTAINS(LCASE(str(?dataset)), "minds")
    )
}
ORDER BY ?name
LIMIT 20
"""

# Datasets by species
DATASETS_BY_SPECIES = """
PREFIX openminds: <https://openminds.ebrains.eu/vocab/>
PREFIX schema: <https://schema.org/>

SELECT ?dataset ?name ?species ?speciesName
WHERE {
    ?dataset a openminds:Dataset ;
             schema:name ?name ;
             openminds:studiedSpecies ?species .
    
    ?species schema:name ?speciesName .
    
    VALUES ?speciesName { "Homo sapiens" "Mus musculus" "Rattus norvegicus" }
}
ORDER BY ?speciesName ?name
LIMIT 30
"""

# Datasets with spatial information
SPATIAL_DATASETS = """
PREFIX openminds: <https://openminds.ebrains.eu/vocab/>
PREFIX sands: <https://openminds.ebrains.eu/sands/>
PREFIX schema: <https://schema.org/>

SELECT ?dataset ?name ?atlas ?region ?coordinates
WHERE {
    ?dataset a openminds:Dataset ;
             schema:name ?name ;
             openminds:spatialLocation ?location .
    
    OPTIONAL {
        ?location sands:atlas ?atlas .
    }
    
    OPTIONAL {
        ?location sands:brainRegion ?region .
    }
    
    OPTIONAL {
        ?location sands:coordinates ?coordinates .
    }
}
LIMIT 25
"""

# Temporal datasets (longitudinal studies)
TEMPORAL_DATASETS = """
PREFIX openminds: <https://openminds.ebrains.eu/vocab/>
PREFIX schema: <https://schema.org/>

SELECT ?dataset ?name ?timepoint ?duration
WHERE {
    ?dataset a openminds:Dataset ;
             schema:name ?name ;
             openminds:hasTimepoint ?timepoint .
    
    OPTIONAL {
        ?dataset openminds:studyDuration ?duration .
    }
    
    FILTER(?timepoint > "2020-01-01"^^xsd:date)
}
ORDER BY DESC(?timepoint)
LIMIT 20
"""

# Datasets with file information
DATASETS_WITH_FILES = """
PREFIX openminds: <https://openminds.ebrains.eu/vocab/>
PREFIX schema: <https://schema.org/>

SELECT ?dataset ?name ?file ?fileFormat ?fileSize
WHERE {
    ?dataset a openminds:Dataset ;
             schema:name ?name ;
             openminds:hasFile ?file .
    
    ?file openminds:format ?fileFormat ;
          openminds:contentSize ?fileSize .
}
ORDER BY DESC(?fileSize)
LIMIT 15
"""

# Software and tools related to MINDS
MINDS_SOFTWARE = """
PREFIX openminds: <https://openminds.ebrains.eu/vocab/>
PREFIX schema: <https://schema.org/>

SELECT ?software ?name ?version ?description ?license
WHERE {
    ?software a openminds:Software ;
              schema:name ?name ;
              schema:description ?description .
    
    OPTIONAL {
        ?software openminds:version ?version .
    }
    
    OPTIONAL {
        ?software openminds:license ?license .
    }
    
    FILTER(
        CONTAINS(LCASE(?description), "minds") ||
        CONTAINS(LCASE(?name), "neuroshape") ||
        CONTAINS(LCASE(?name), "fair")
    )
}
LIMIT 20
"""

# Complex federated query example
FEDERATED_BRAIN_REGIONS = """
PREFIX openminds: <https://openminds.ebrains.eu/vocab/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT ?dataset ?name ?region ?regionLabel
WHERE {
    ?dataset a openminds:Dataset ;
             schema:name ?name ;
             openminds:studiedBrainRegion ?region .
    
    SERVICE <https://query.wikidata.org/sparql> {
        ?region rdfs:label ?regionLabel .
        FILTER(LANG(?regionLabel) = "en")
    }
}
LIMIT 10
"""

# All available query templates
QUERY_TEMPLATES = {
    'basic_minds': FIND_MINDS_DATASETS,
    'by_species': DATASETS_BY_SPECIES, 
    'spatial': SPATIAL_DATASETS,
    'temporal': TEMPORAL_DATASETS,
    'with_files': DATASETS_WITH_FILES,
    'software': MINDS_SOFTWARE,
    'federated': FEDERATED_BRAIN_REGIONS
}
