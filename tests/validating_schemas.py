import sys,os
import pytest
import logging
from validator_helper import Validator


def test_valid_schema_file(shacl_validator, schema_file):
    try:
        shacl_validator.load_schema(schema_file)
    except:
        pytest.fail(f'Invalid schema {schema_file}')


def test_valid_data(data_shape_file, test_file, test_valid):

    conforms, results, report = make_validation(data_shape_file, test_file)
    if test_valid:
        assert conforms, report
    else:
        assert conforms==False, report
        assert results == 1, "Validation report expects only 1 entry"


def make_validation(data_shape_file, test_file):
    base_dir = data_shape_file.replace(os.path.join('examples','datashapes.json'),'')
    schema_file = base_dir +'schema.json'
    data_validator = Validator(pytest.SHACL_SHACL)
    data_validator.load_schema(schema_file)
    data_validator.load_schema(data_shape_file, aggregate=True)

    return data_validator.validate_data_file(test_file)
