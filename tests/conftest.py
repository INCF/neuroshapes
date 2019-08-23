import os, sys
import pytest
import logging
import glob
from validator_helper import Validator

logger = logging.getLogger(__name__)

PATH = os.getcwd()
SHACL_SHACL = os.path.join(PATH, 'tests','shacl-schema.ttl')

if not os.path.exists(SHACL_SHACL):
    logger.error(f'{SHACL_SHACL} not found')
    sys.exit()

@pytest.fixture(scope='session')
def shacl_validator():
    logger.info("creating shacl validator")
    shacl_validator = Validator(SHACL_SHACL)
    return shacl_validator


def pytest_generate_tests(metafunc):

    scan_dir = os.path.join(PATH, '..','neuroshapes','shapes','neurosciencegraph','commons')
    schema_files = [f for f in glob.iglob( scan_dir + '/**/schema.json', recursive=True)]

    if "schema_file" in metafunc.fixturenames:
        metafunc.parametrize("schema_file", schema_files)
