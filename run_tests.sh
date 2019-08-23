python3 -m venv env
source env/bin/activate
pip install --upgrade pip  # not sure this is needed
pip install pyshacl
pip install pytest
# fix owlrl issue  https://github.com/RDFLib/OWL-RL/issues/29#issuecomment-484773978
mv env/bin/owlrl.py env/bin/owlrl
# run tests
pytest tests/validating_schemas_pytest.py

# clean TestSuite
deactivate
rm -r env # not sure this is needed
