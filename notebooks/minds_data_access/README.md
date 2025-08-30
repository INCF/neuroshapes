# MINDS Data Access Tutorial: SPARQL and API Guide

This comprehensive tutorial demonstrates how to access MINDS (Metadata for IN-silico Neuroscience and Data Sharing) data from the EBRAINS Knowledge Graph using SPARQL queries and REST APIs.

## 🎯 Purpose

This tutorial directly addresses **Issue #374** and **Issue #147** from the INCF/neuroshapes repository by providing:

- Complete SPARQL endpoint documentation for MINDS data
- Working Python examples for data access
- Multiple authentication and access methods
- Data visualization and analysis examples
- Integration patterns with neuroshapes schemas

## 🚀 Quick Start

### Prerequisites

1. **Python 3.7+** installed
2. **EBRAINS account** (optional, for full access): [Register here](https://ebrains.eu/register)
3. **Basic understanding** of Python and data analysis

### Installation

# MINDS Data Access Tutorial: SPARQL and API Guide

This comprehensive tutorial demonstrates how to access MINDS (Metadata for IN-silico Neuroscience and Data Sharing) data from the EBRAINS Knowledge Graph using SPARQL queries and REST APIs.

## 🎯 Purpose

This tutorial directly addresses **Issue #374** and **Issue #147** from the INCF/neuroshapes repository by providing:

- Complete SPARQL endpoint documentation for MINDS data
- Working Python examples for data access
- Multiple authentication and access methods
- Data visualization and analysis examples
- Integration patterns with neuroshapes schemas

## 🚀 Quick Start

### Prerequisites

1. **Python 3.7+** installed
2. **EBRAINS account** (optional, for full access): [Register here](https://ebrains.eu/register)
3. **Basic understanding** of Python and data analysis

### Installation

**Clone the repository**
git clone https://github.com/YOUR_USERNAME/neuroshapes.git
cd neuroshapes/notebooks/minds_data_access

**Install dependencies**
pip install -r requirements.txt

**Launch Jupyter**
jupyter notebook minds_sparql_tutorial.ipynb


## 📚 What's Included

### Files

- **`minds_sparql_tutorial.ipynb`** - Main tutorial notebook with interactive examples
- **`config.py`** - Configuration settings and endpoints
- **`minds_queries.py`** - Collection of predefined SPARQL queries
- **`requirements.txt`** - Python dependencies
- **`README.md`** - This documentation

### Tutorial Sections

1. **🔐 Authentication Setup** - EBRAINS token configuration
2. **🔍 Basic Data Discovery** - Finding MINDS datasets
3. **💬 SPARQL Queries** - Advanced querying examples
4. **🌐 Public API Access** - No-authentication methods
5. **📊 Data Visualization** - Charts and analytics
6. **🔄 Interactive Explorer** - GUI-based data exploration
7. **🔗 Integration Examples** - Linking with other resources
8. **💡 Best Practices** - Performance and reliability tips
9. **🔧 Troubleshooting** - Common issues and solutions

## 🎯 Access Methods Covered

### 1. SPARQL Endpoints

- **Primary Endpoint**: `https://core.kg.ebrains.eu/v3-beta/queries`
- **Authentication**: Bearer token required for full access
- **Query Language**: SPARQL 1.1 with EBRAINS extensions

### 2. REST APIs

- **Search API**: `https://search.kg.ebrains.eu/api/search` (public)
- **Knowledge Graph API**: `https://core.kg.ebrains.eu/v3-beta/` (authenticated)
- **Dataset Details API**: Individual dataset access

### 3. Python SDK

- **EBRAINS KG Core**: Official Python client library
- **Features**: High-level data access, authentication handling, result processing

## 🔍 Example Queries

### Find MINDS Datasets

PREFIX openminds: https://openminds.ebrains.eu/vocab/
PREFIX schema: https://schema.org/

SELECT DISTINCT ?dataset ?name ?description
WHERE {
?dataset a openminds:Dataset ;
schema:name ?name ;
schema:description ?description .

FILTER(CONTAINS(LCASE(?description), "minds"))
}
LIMIT 20


### Species-Specific Data

PREFIX openminds: https://openminds.ebrains.eu/vocab/

SELECT ?dataset ?name ?species
WHERE {
?dataset a openminds:Dataset ;
schema:name ?name ;
openminds:studiedSpecies ?species .
VALUES ?species { "Homo sapiens" "Mus musculus" }
}


## 🔐 Authentication

### Option 1: Environment Variable (Recommended)

export EBRAINS_TOKEN="your_token_here"


### Option 2: Direct Configuration

from config import EBRAINSAuthenticator

auth = EBRAINSAuthenticator()
auth.setup_authentication("your_token_here")


### Getting Your Token

1. Register at [EBRAINS](https://ebrains.eu/register)
2. Go to your [profile page](https://ebrains.eu/page/profile)
3. Generate a new API token
4. Copy and use in your code

## 📊 Data Types Available

- **Neuroanatomical Datasets** - Brain structure data
- **Electrophysiology** - Neural recording data
- **Neuroimaging** - MRI, fMRI, PET scans
- **Behavioral Data** - Cognitive and behavioral studies
- **Computational Models** - Brain simulation models
- **Software Tools** - Analysis and visualization tools
- **Metadata Schemas** - Data structure definitions

## 🌐 No-Authentication Access

For users without EBRAINS accounts, the tutorial includes:

- Public dataset search functionality
- Demo data for learning SPARQL
- Visualization examples with sample data
- Links to publicly available resources

## 🔗 Integration Examples

### With Neuroshapes

Validate MINDS data against neuroshapes schemas
from rdflib import Graph
import requests

def validate_dataset(dataset_uri):
# Load dataset metadata
dataset_graph = Graph()
dataset_graph.parse(dataset_uri)


# Apply neuroshapes validation
# (Implementation details in notebook)
return validation_results

### With Brain Atlases

Link datasets to anatomical regions
SELECT ?dataset ?region ?coordinates
WHERE {
?dataset openminds:spatialLocation ?location .
?location sands:brainRegion ?region ;
sands:coordinates ?coordinates .
}


## 📈 Analytics Features

- **Species Distribution** - Pie charts of data by organism
- **Technique Analysis** - Bar charts of experimental methods  
- **Temporal Trends** - Growth of data over time
- **Size Analysis** - Dataset size distributions
- **Interactive Dashboards** - GUI-based exploration

## 🛠 Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Check token validity
   - Verify correct header format
   - Ensure sufficient permissions

2. **Query Timeouts**
   - Add LIMIT clauses
   - Optimize query structure
   - Use specific filters

3. **Empty Results**
   - Verify query syntax
   - Check namespace prefixes
   - Start with broader queries

4. **Network Issues**
   - Check internet connectivity
   - Verify endpoint URLs
   - Implement retry logic

### Getting Help

- **EBRAINS Support**: [support@ebrains.eu](mailto:support@ebrains.eu)
- **INCF Community**: [GitHub Discussions](https://github.com/INCF/neuroshapes/discussions)
- **Documentation**: [EBRAINS Docs](https://docs.ebrains.eu/)

## 🚀 Next Steps

After completing this tutorial, you can:

1. **Explore Advanced Queries** - Complex SPARQL patterns
2. **Build Custom Applications** - Using the provided APIs
3. **Contribute to Neuroshapes** - Add new schemas or tools
4. **Share Your Work** - Publish findings or tools
5. **Join the Community** - Participate in INCF projects

## 📝 Contributing

Found an issue or want to improve the tutorial?

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📄 License

This tutorial is licensed under CC-BY-4.0, same as the neuroshapes project.

## 🙏 Acknowledgments

- **EBRAINS Platform** - For providing the infrastructure
- **INCF Community** - For neuroshapes and standards development
- **Contributors** - Everyone who helped improve this tutorial

---

**Issues Addressed**: This tutorial directly solves INCF/neuroshapes Issues #374 and #147 by providing comprehensive SPARQL access documentation and working Python examples for MINDS data access.
