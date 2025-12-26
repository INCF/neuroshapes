# YAML Templates for Neuroshapes

Human-readable templates for manual data entry. These templates can be filled out and converted to JSON-LD for validation.

## Usage

1. Copy the relevant template file
2. Fill in your experimental data
3. Convert to JSON-LD using `scripts/yaml_to_jsonld.py`
4. Validate against Neuroshapes schemas

## Available Templates

- `subject.yaml` - Subject/animal information
- `slice.yaml` - Brain slice preparation
- `patched_slice.yaml` - Electrophysiology recording
- `reconstructed_cell.yaml` - Complete neuron reconstruction workflow

## Example

```bash
# Copy a template
cp templates/yaml/subject.yaml my_experiment.yaml

# Edit with your data
nano my_experiment.yaml

# Convert to JSON-LD
python scripts/yaml_to_jsonld.py my_experiment.yaml my_experiment.json

# Validate (optional)
python scripts/yaml_to_jsonld.py my_experiment.yaml my_experiment.json --validate
```

## Why YAML?

- **Human-readable**: Cleaner syntax than JSON
- **Less error-prone**: No bracket matching issues
- **Compact**: Uses indentation instead of separators
- **JSON-compatible**: YAML is a superset of JSON
- **Better for manual editing**: Easier to see hierarchy

## Contributing

When creating new templates:
1. Follow the existing naming convention
2. Include helpful comments for each field
3. Provide example values where appropriate
4. Test conversion to JSON-LD
