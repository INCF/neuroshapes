import os, sys
import pytest
import logging
import glob
from shaclvalidator import get_graph
from shaclvalidator import Validator

logger = logging.getLogger(__name__)

PATH = os.getcwd()
pytest.SHACL_SHACL = os.path.join(PATH, 'tests', 'shacl-schema.ttl')

if not os.path.exists(pytest.SHACL_SHACL):
    logger.error(f'{pytest.SHACL_SHACL} not found')
    sys.exit()


@pytest.fixture(scope='session')
def shacl_schema():
    logger.info("loading SHACL of SHACL schema")
    return get_graph(pytest.SHACL_SHACL)


def pytest_addoption(parser):
    default_scan_dir = os.path.join(PATH, '..', 'neuroshapes', 'shapes')
    parser.addoption("--scan_dir", action="store", default=default_scan_dir)


def pytest_generate_tests(metafunc):

    # perform schemas validation
    scan_dir = metafunc.config.option.scan_dir
    logger.info(f'scanning {scan_dir}')

    schema_files = [f for f in glob.iglob(scan_dir + '/**/schema.json', recursive=True)]

    datashape_files = [f.replace('schema.json', os.path.join('examples', 'datashapes.json')) for f in schema_files]
    datashape_files = list(filter(lambda f: os.path.exists(f), datashape_files))
    shapes_files = schema_files + datashape_files

    if "schema_file" in metafunc.fixturenames:
        metafunc.parametrize("schema_file", shapes_files)

    tests_payload = []
    for sh in schema_files:

        subdir = sh.replace(os.sep + 'schema.json', '')

        if not os.path.exists(os.sep.join([subdir, 'examples'])):
            continue

        shape_file = sh
        datashape_example = os.sep.join([subdir, 'examples', 'datashapes.json'])
        if os.path.exists(datashape_example):
            shape_file = datashape_example

        valid_dir = os.sep.join([subdir, 'examples', 'valid']) + os.sep
        if os.path.exists(valid_dir):
            for f in glob.glob(valid_dir + '*.json'):
                tests_payload.append((shape_file, f, True))

        invalid_dir = os.sep.join([subdir, 'examples', 'invalid']) + os.sep
        if os.path.exists(invalid_dir):
            for f in glob.glob(invalid_dir + '*.json'):
                tests_payload.append((shape_file, f, False))

    if set(['shapes_file', 'test_file', 'test_valid']).issubset(set(metafunc.fixturenames)):
        metafunc.parametrize('shapes_file, test_file, test_valid', tests_payload)
