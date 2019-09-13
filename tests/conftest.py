import os, sys
import pytest
import logging
import glob
from shaclvalidator import get_graph

logger = logging.getLogger(__name__)

PATH = os.getcwd()
pytest.SHACL_SHACL = os.path.join(PATH, 'tests','shacl-schema.ttl')

if not os.path.exists(pytest.SHACL_SHACL):
    logger.error(f'{pytest.SHACL_SHACL} not found')
    sys.exit()


@pytest.fixture(scope='session')
def shacl_schema():
    logger.info("loading SHACL of SHACL schema")
    return get_graph(pytest.SHACL_SHACL)


def pytest_addoption(parser):
    default_scan_dir = os.path.join(PATH, '..','neuroshapes','shapes')
    parser.addoption("--scan_dir", action="store", default=default_scan_dir)


def pytest_generate_tests(metafunc):

    # perform schemas validation
    scan_dir = metafunc.config.option.scan_dir
    logger.info(f'scanning {scan_dir}')

    schema_files = [f for f in glob.iglob( scan_dir + '/**/schema.json', recursive=True)]

    datashape_files = [f.replace('schema.json', os.path.join('examples','datashapes.json')) for f in schema_files]
    datashape_files = list(filter(lambda f: os.path.exists(f), datashape_files))
    shapes_files = schema_files + datashape_files

    if "schema_file" in metafunc.fixturenames:
        metafunc.parametrize("schema_file", shapes_files)

    test_sets = []
    for sh in schema_files:

        valid_dir = sh.replace('schema.json', os.path.join('examples','valid')) + os.path.sep
        if os.path.exists(valid_dir):
            for f in glob.glob(valid_dir + '*.json'):
                test_sets.append((sh, f, True))

        invalid_dir = sh.replace('schema.json', os.path.join('examples','invalid')) + os.path.sep
        if os.path.exists(invalid_dir):
            for f in glob.glob(invalid_dir + '*.json'):
                test_sets.append((sh, f, False))

    if set(['data_shape_file', 'test_file', 'test_valid']).issubset(set(metafunc.fixturenames)):
        metafunc.parametrize('data_shape_file, test_file, test_valid', test_sets)
