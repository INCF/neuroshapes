"""Tests for YAML templates and conversion"""
import pytest
import yaml
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.yaml_to_jsonld import yaml_to_jsonld, clean_entity, TYPE_MAPPINGS

TEMPLATES_DIR = Path(__file__).parent.parent / "templates" / "yaml"


def test_yaml_templates_exist():
    """Ensure all expected YAML templates are present."""
    expected_templates = [
        "subject.yaml",
        "slice.yaml",
        "patched_slice.yaml",
        "reconstructed_cell.yaml"
    ]
    
    for template in expected_templates:
        template_path = TEMPLATES_DIR / template
        assert template_path.exists(), f"Missing template: {template}"


def test_yaml_templates_valid_syntax():
    """Ensure all YAML templates have valid syntax."""
    for yaml_file in TEMPLATES_DIR.glob("*.yaml"):
        if yaml_file.name == "README.md":
            continue
        with open(yaml_file) as f:
            data = yaml.safe_load(f)
            assert data is not None, f"Invalid YAML in {yaml_file}"


def test_yaml_to_jsonld_conversion():
    """Test conversion from YAML to JSON-LD."""
    sample_yaml = {
        "Subject": {
            "id": "subject001",
            "species": "Mus musculus",
            "strain": "C57BL/6"
        }
    }
    
    result = yaml_to_jsonld(sample_yaml)
    
    assert "@context" in result
    assert "@graph" in result
    assert len(result["@graph"]) == 1
    assert result["@graph"][0]["@type"] == TYPE_MAPPINGS["Subject"]
    assert result["@graph"][0]["id"] == "subject001"


def test_empty_fields_removed():
    """Test that empty fields are removed during conversion."""
    sample_yaml = {
        "Subject": {
            "id": "subject001",
            "species": "",
            "strain": None
        }
    }
    
    result = yaml_to_jsonld(sample_yaml)
    subject = result["@graph"][0]
    
    assert "id" in subject
    assert "species" not in subject
    assert "strain" not in subject


def test_clean_entity():
    """Test entity cleaning function."""
    dirty = {
        "id": "test",
        "empty": "",
        "none": None,
        "valid": "data",
        "nested": {
            "kept": "value",
            "removed": ""
        }
    }
    
    cleaned = clean_entity(dirty)
    
    assert "id" in cleaned
    assert "empty" not in cleaned
    assert "none" not in cleaned
    assert "valid" in cleaned
    assert "nested" in cleaned
    assert "kept" in cleaned["nested"]
    assert "removed" not in cleaned["nested"]


def test_multiple_entities():
    """Test conversion with multiple entity types."""
    sample_yaml = {
        "Subject": {"id": "S1", "species": "Mouse"},
        "Slice": {"protocol": "P1", "person": "Researcher"}
    }
    
    result = yaml_to_jsonld(sample_yaml)
    
    assert len(result["@graph"]) == 2
    types = [entity["@type"] for entity in result["@graph"]]
    assert TYPE_MAPPINGS["Subject"] in types
    assert TYPE_MAPPINGS["Slice"] in types


def test_nested_coordinates():
    """Test conversion with nested structures like coordinates."""
    sample_yaml = {
        "LabeledCell": {
            "name": "cell01",
            "coordinatesInBrainAtlas": {
                "rostrocaudal": "1.2",
                "lateral": "2.3",
                "dorsal": "3.4"
            }
        }
    }
    
    result = yaml_to_jsonld(sample_yaml)
    cell = result["@graph"][0]
    
    assert "coordinatesInBrainAtlas" in cell
    assert cell["coordinatesInBrainAtlas"]["rostrocaudal"] == "1.2"
