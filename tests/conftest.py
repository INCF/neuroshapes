"""Tests generation and configuration"""
import glob
import logging
import os
from typing import List, Tuple

import pytest
import sys
from rdflib import Graph

from tests.shaclvalidator import add_file_to_graph

LOGGER = logging.getLogger(__name__)


def pytest_configure():
    """Initializes pytest.shape_to_file variable with the mapping of shapes_id to its file"""
    pytest.path_to_namespace = {
        "shapes/prov/datashapes": "https://neuroshapes.org/dash",
        "shapes/prov/commons": "https://provshapes.org/commons",
        "shapes/neurosciencegraph/datashapes": "https://neuroshapes.org/dash",
        "shapes/neurosciencegraph/commons": "https://neuroshapes.org/commons"
    }
    pytest.shape_to_file = dict()
    for subdir, namespace in pytest.path_to_namespace.items():
        pytest.shape_to_file.update(scan_shapes(subdir, namespace))


@pytest.fixture(scope="session")
def shacl_schema():
    """Provide an in memory graph with the SHACL schema"""
    SHACL_SHACL = os.path.join("tests", "shacl-schema.ttl")
    if not os.path.exists(SHACL_SHACL):
        LOGGER.error("%s not found", SHACL_SHACL)
        sys.exit()
    graph = Graph()
    add_file_to_graph(graph, SHACL_SHACL)
    return graph


def pytest_addoption(parser):
    """Retrieve a parameter to test specific directory"""
    parser.addoption("--testdir", action="store", default=None,
                     help="test shapes inside a specific directory")


def pytest_generate_tests(metafunc):
    """Generates tests for shapes and examples"""

    examples_files = list()
    schemas_files = dict()
    if metafunc.config.option.testdir:
        directory = metafunc.config.option.testdir
        if os.path.exists(directory):
            for subdir, namespace in pytest.path_to_namespace.items():
                if directory.startswith(subdir):
                    schemas_files = scan_shapes(directory, namespace).values()
        else:
            LOGGER.error("%s not found", directory)
            sys.exit()
    else:
        schemas_files = pytest.shape_to_file.values()
        for subdir, _ in pytest.path_to_namespace.items():
            examples_files.extend(scan_examples(subdir))

    if "schema_file" in metafunc.fixturenames:
        metafunc.parametrize("schema_file", schemas_files)

    if "shapes_file" in metafunc.fixturenames:
        metafunc.parametrize("shapes_file,test_file,assertion", examples_files)


def scan_shapes(path, ns):
    cwd = os.getcwd()
    abs_path = os.path.join(cwd, path)
    shape_file = dict()
    for path_file in glob.iglob(abs_path + "/**/schema.json", recursive=True):
        uri = path_file.replace(abs_path, ns).replace("/schema.json", "")
        shape_file[uri] = path_file
    return shape_file


def scan_examples(path) -> List[Tuple[str, list, bool]]:
    cwd = os.getcwd()
    ex_path = path.replace("shapes", "examples", 1)
    abs_path = os.path.join(cwd, ex_path)
    examples: List[Tuple[str, list, bool]] = list()
    schemas = [os.path.split(f)[0] for f in glob.glob(abs_path + "/**/schema.json", recursive=True)]

    for v in glob.glob(abs_path + "/**/valid/*.json", recursive=True):
        head, _ = v.split("/valid")
        schema = get_schema(head, schemas)
        examples.append((schema, v, True))

    for v in glob.glob(abs_path + "/**/invalid/*.json", recursive=True):
        head, _ = v.split("/invalid")
        schema = get_schema(head, schemas)
        examples.append((schema, v, False))

    return examples


def get_schema(path, schemas):
    if path in schemas:
        return f"{path}/schema.json"
    else:
        return f"{path.replace('examples', 'shapes', 1)}/schema.json"
