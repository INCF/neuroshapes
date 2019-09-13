import os
import pytest
from shaclvalidator import Validator
from shaclvalidator import run_validation
from shaclvalidator import get_graph


def test_valid_schema_file(shacl_schema, schema_file):
    graph = get_graph(schema_file)
    conforms, res, report = run_validation(graph, shacl_schema)
    assert conforms, "shape does not conform with SHACL of SHACL: " + report


def test_valid_data(data_shape_file, test_file, test_valid):
    conforms, results, report = make_validation(data_shape_file, test_file)
    if test_valid:
        assert conforms, report
    else:
        assert conforms is False, report
        assert results == 1, "Validation report expects only 1 entry"


def make_validation(shapes_file, test_file):
    data_validator = Validator(pytest.SHACL_SHACL)
    data_validator.load_schema(shapes_file)
    datashape_example = shapes_file.replace('schema.json', os.path.join('examples', 'datashapes.json'))

    if os.path.exists(datashape_example):
        data_validator.load_schema(datashape_example, aggregate=True)

    return data_validator.validate_data_file(test_file)
