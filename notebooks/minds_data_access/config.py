"""
Configuration for MINDS data access tutorial
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# EBRAINS Configuration
EBRAINS_BASE_URL = "https://core.kg.ebrains.eu"
EBRAINS_SEARCH_URL = "https://search.kg.ebrains.eu"
EBRAINS_KG_API_V3 = "https://core.kg.ebrains.eu/v3-beta"

# SPARQL Endpoints
SPARQL_ENDPOINTS = {
    'ebrains_kg': f"{EBRAINS_KG_API_V3}/queries",
    'public_search': f"{EBRAINS_SEARCH_URL}/api/search"
}

# Authentication
EBRAINS_TOKEN = os.getenv('EBRAINS_TOKEN', None)

# Query configurations
DEFAULT_LIMIT = 50
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Data types and filters
MINDS_DATA_TYPES = [
    'Dataset',
    'DatasetVersion', 
    'Model',
    'Software',
    'WebService'
]

SPECIES_FILTERS = [
    'Homo sapiens',
    'Mus musculus', 
    'Rattus norvegicus',
    'Macaca mulatta'
]

TECHNIQUE_FILTERS = [
    'electrophysiology',
    'neuroimaging', 
    'microscopy',
    'behavioral'
]
