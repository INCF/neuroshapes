from pyshacl import validate
import rdflib
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG


SH = rdflib.Namespace('http://www.w3.org/ns/shacl#')
RDF = rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')

def get_graph(file):
    filetype = rdflib.util.guess_format(file)
    if filetype == None:
        filetype="json-ld"
    graph = rdflib.Graph()
    graph.parse(file, format=filetype)
    return graph

class Validator:

    def __init__(self, shacl_schema_file):
        self.shacl_schema = get_graph(shacl_schema_file)
        self.schema_graph = None

    def load_schema(self, schema_file, aggregate=False):
        schema_tmp = get_graph(schema_file)
        if not aggregate :
            self.schema_graph = rdflib.Graph()
        conforms, res, report = self.run_validation(schema_tmp, self.shacl_schema)
        if conforms:
            self.schema_graph = self.schema_graph + schema_tmp
            logger.debug(f'{schema_file} loaded with {len(schema_tmp)} triples')
        else:
            msg = f'Invalid schema {schema_file}'
            logger.error(msg)
            logger.error(report)
            raise Exception(msg)

    def validate_data_file(self, data_file):
        data_graph = get_graph(data_file)
        return self.run_validation(data_graph, self.schema_graph)

    def run_validation(self, data, schema):
        conforms, v_graph, v_text = validate(data, shacl_graph=schema, inference='rdfs', debug=False)
        results = [r for r in v_graph.triples( (None, RDF.type, SH.ValidationResult) )]
        return (conforms, len(results), v_text)
