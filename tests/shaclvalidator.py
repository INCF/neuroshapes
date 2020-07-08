import logging
from typing import Tuple, List, Any

from pyshacl import validate
from rdflib import Graph, Namespace
from rdflib.util import guess_format


LOGGER = logging.getLogger(__name__)

SH = Namespace('http://www.w3.org/ns/shacl#')
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')


def add_file_to_graph(graph: Graph, file: str, imports_map=None, imported: List[str] = None) -> Graph:
    """Returns a graph with the loaded rdf file

    Args:
        :param graph: graph to be used to parse the file
        :param file: Rdf file to load
        :param imports_map: a uri to file map
        :param imported: collected imports from previous parsed files
    Return:
        :return: Graph
    """

    if imports_map is None:
        imports_map = {}
    if imported is None:
        imported = []
    file_type = guess_format(file)
    if file_type is None:
        file_type = "json-ld"
    graph.parse(file, format=file_type)
    for obj in graph.objects(None, OWL.imports):
        try:
            local = imports_map[str(obj)]
            if local not in imported:
                imported.append(local)
                add_file_to_graph(graph, local, imports_map, imported)
        except KeyError:
            LOGGER.error("%s not in map", str(obj))

    return graph


def run_validation(data: Graph, schema: Graph) -> Tuple[Any, int, Any]:
    """Runs the validation of data against a schema

    Args:
        :param data: the data to validate in a graph
        :param schema: the schema to use to validate the data

    Return:
        :return: a tuple: conforms, results in a graph, results
    """
    conforms, v_graph, v_text = validate(
        data, shacl_graph=schema, inference="rdfs", debug=False)
    results = list(v_graph.triples((None, RDF.type, SH.ValidationResult)))
    return conforms, len(results), v_text
