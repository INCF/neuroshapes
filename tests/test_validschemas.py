from shaclvalidator import Validator
from shaclvalidator import run_validation
from shaclvalidator import get_graph
import pytest
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG


def test_valid_schema_file(shacl_schema, schema_file):
    logger.debug(f'validating {schema_file}')
    graph = get_graph(schema_file, [])
    conforms, res, report = run_validation(graph, shacl_schema)
    assert conforms, "shape does not conform with SHACL of SHACL: " + report


def test_examples(shapes_file: str, test_file: str, test_valid: bool):
    validator = Validator(pytest.SHACL_SHACL)
    validator.load_schema(shapes_file)
    conforms, results, report = validator.validate_data_file(test_file)
    if test_valid:
        assert conforms, report
    else:
        assert conforms is False, "validation should fail"
        assert results == 1, "Validation report expects only 1 entry"
