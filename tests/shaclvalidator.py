from pyshacl import validate
import rdflib
import logging
import os

logger = logging.getLogger()
logger.level = logging.DEBUG

SH = rdflib.Namespace('http://www.w3.org/ns/shacl#')
RDF = rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
OWL = rdflib.namespace.Namespace('http://www.w3.org/2002/07/owl#')

IMPORTS_MAP = {
    "https://provshapes.org": "shapes/prov",
    "https://neuroshapes.org/commons": "shapes/neurosciencegraph/commons",
    "https://neuroshapes.org/dash": "shapes/neurosciencegraph/datashapes",
}


def get_local(resource):
    path = os.getcwd()
    for key in IMPORTS_MAP:
        if resource.startswith(key):
            return os.sep.join([path, resource.replace(key, IMPORTS_MAP[key]) ,'schema.json'])


def get_graph(file, imports=[]):
    file_type = rdflib.util.guess_format(file)
    if file_type is None:
        file_type = "json-ld"
    graph = rdflib.Graph()
    graph.parse(file, format=file_type)
    for o in graph.objects(None, OWL.imports):
        local = get_local(o)
        if local in imports:
            continue
        else:
            # this will avoid loading resource more than once
            imports.append(local)
            if os.path.exists(local):
                logging.info(f'importing {o} as {local}')
                imported_graph = get_graph(local, imports)
                graph += imported_graph
            else:
                logger.error(f'Could not import {local}, it does not exist')

    return graph


def run_validation(data, schema):
    conforms, v_graph, v_text = validate(data, shacl_graph=schema, inference='rdfs', debug=False)
    results = [r for r in v_graph.triples((None, RDF.type, SH.ValidationResult))]
    return conforms, len(results), v_text


class Validator:

    def __init__(self, shacl_schema_file):
        self.shacl_schema = get_graph(shacl_schema_file, [])
        self.schema_graph = None

    def load_schema(self, schema_file,):
        logger.debug(f'loading {schema_file}')
        self.schema_graph = get_graph(schema_file, [])
        conforms, res, report = run_validation(self.schema_graph , self.shacl_schema)
        if not conforms:
            msg = f'Invalid schema {schema_file}'
            logger.error(msg)
            logger.error(report)
            raise Exception(msg)

    def validate_data_file(self, data_file):

        data_graph = get_graph(data_file)
        return run_validation(data_graph, self.schema_graph)
