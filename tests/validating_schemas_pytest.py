import sys
import pytest
import logging

logger = logging.getLogger(__name__)


def test_valid_shape_file(shacl_validator, schema_file):
    try:
        shacl_validator.load_schema(schema_file)
    except:
        pytest.fail(f'Invalid schema {schema_file}')
