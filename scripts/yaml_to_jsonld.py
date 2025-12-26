#!/usr/bin/env python3
"""
Convert YAML templates to JSON-LD format compatible with Neuroshapes schemas.

Usage:
    python yaml_to_jsonld.py input.yaml output.json
    python yaml_to_jsonld.py input.yaml output.json --validate
"""

import yaml
import json
import sys
from pathlib import Path
from typing import Dict, Any

CONTEXT = "https://incf.github.io/neuroshapes/contexts/data.json"

TYPE_MAPPINGS = {
    "Subject": "nsg:Subject",
    "Slice": "nsg:Slice",
    "PatchedSlice": "nsg:PatchedSlice",
    "FixedStainedSlice": "nsg:FixedStainedSlice",
    "ImagedSlice": "nsg:ImagedSlice",
    "LabeledCell": "nsg:LabeledCell",
    "ReconstructedCell": "nsg:ReconstructedCell"
}


def clean_entity(entity_data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove empty fields from entity data."""
    cleaned = {}
    for key, value in entity_data.items():
        if value == "" or value is None:
            continue
        if isinstance(value, dict):
            nested = clean_entity(value)
            if nested:
                cleaned[key] = nested
        else:
            cleaned[key] = value
    return cleaned


def yaml_to_jsonld(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert YAML structure to JSON-LD with proper @type and @context."""
    jsonld = {
        "@context": CONTEXT,
        "@graph": []
    }
    
    for entity_type, entity_data in yaml_data.items():
        if entity_type not in TYPE_MAPPINGS:
            continue
            
        if not entity_data:
            continue
            
        cleaned_data = clean_entity(entity_data)
        if not cleaned_data:
            continue
            
        entity = {
            "@type": TYPE_MAPPINGS[entity_type],
            **cleaned_data
        }
        jsonld["@graph"].append(entity)
    
    return jsonld


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    if not input_path.exists():
        print(f"Error: Input file {input_path} not found")
        sys.exit(1)
    
    try:
        with open(input_path) as f:
            yaml_data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)
    
    jsonld_data = yaml_to_jsonld(yaml_data)
    
    with open(output_path, 'w') as f:
        json.dump(jsonld_data, f, indent=2)
    
    print(f"Converted {input_path} to {output_path}")
    
    if "--validate" in sys.argv:
        print("\nNote: Validation against SHACL schemas not yet implemented")
        print("Please use existing validation tools in tests/")


if __name__ == "__main__":
    main()
