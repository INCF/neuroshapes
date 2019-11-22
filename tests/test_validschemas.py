"""Testing functions"""
import logging

import pytest
from rdflib import Graph

from tests.shaclvalidator import add_file_to_graph, run_validation

LOGGER = logging.getLogger(__name__)


def test_valid_schema_file(shacl_schema: Graph, schema_file: str):
    """Validates a SHACL shape conforms to a SHACL schema

    Args:
        :param shacl_schema: the graph whith the SHACL schema loaded
        :param schema_file: the path of the schema to validate
    """
    LOGGER.debug("validating %s", schema_file)
    graph = Graph()
    add_file_to_graph(graph, schema_file, pytest.shape_to_file)
    conforms, _, report = run_validation(graph, shacl_schema)
    assert conforms, "shape does not conform with SHACL of SHACL: " + report
    if conforms is False:
        LOGGER.info(report)


def test_examples(shapes_file, test_file, assertion):
    """Test validity or invalidity of data against a SHACL shape

    Args:
        :param shapes_file: file where the SHACL shape is
        :param test_file: the data file to validate
        :param assertion: specify what to test validity or invalidity
    """
    LOGGER.debug("testing %s", test_file)
    shapes_graph = Graph()
    add_file_to_graph(shapes_graph, shapes_file, pytest.shape_to_file)
    data_graph = Graph()
    add_file_to_graph(data_graph, test_file)
    conforms, results, report = run_validation(data_graph, shapes_graph)

    if assertion:
        assert conforms, report
    else:
        assert conforms is False, "validation should fail"
        assert results == 1, "Validation report expects only 1 entry"
