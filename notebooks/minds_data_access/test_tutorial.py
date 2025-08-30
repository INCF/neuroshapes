"""
Test suite for MINDS data access tutorial
"""

import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__))

import pandas as pd
import requests
from unittest.mock import patch, MagicMock

from config import *
from minds_queries import QUERY_TEMPLATES

class TestMindsDataAccess(unittest.TestCase):
    """Test the MINDS data access functionality"""
    
    def test_config_values(self):
        """Test that configuration values are properly set"""
        self.assertTrue(EBRAINS_BASE_URL.startswith('https://'))
        self.assertTrue(EBRAINS_SEARCH_URL.startswith('https://'))
        self.assertIsInstance(MINDS_DATA_TYPES, list)
        self.assertGreater(len(MINDS_DATA_TYPES), 0)
    
    def test_query_templates(self):
        """Test that all query templates are valid SPARQL"""
        for template_name, query in QUERY_TEMPLATES.items():
            self.assertIsInstance(query, str)
            self.assertIn('SELECT', query.upper())
            self.assertIn('WHERE', query.upper())
    
    @patch('requests.get')
    def test_public_search_api(self, mock_get):
        """Test public search API functionality"""
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'hits': {
                'hits': [
                    {
                        '_id': 'test_123',
                        '_source': {
                            'title': 'Test Dataset',
                            'description': 'Test description',
                            'type': 'Dataset',
                            'species': ['Homo sapiens'],
                            'techniques': ['electrophysiology'],
                            'contributors': [{'name': 'Test Author'}]
                        }
                    }
                ]
            }
        }
        mock_get.return_value = mock_response
        
        # Test the search functionality
        from minds_sparql_tutorial import PublicMindsAccess
        searcher = PublicMindsAccess()
        results = searcher.search_datasets("test")
        
        self.assertIsInstance(results, pd.DataFrame)
        self.assertGreater(len(results), 0)
        self.assertIn('title', results.columns)
    
    def test_sparql_query_construction(self):
        """Test SPARQL query construction"""
        query = QUERY_TEMPLATES['basic_minds']
        
        # Check for required SPARQL elements
        self.assertIn('PREFIX', query)
        self.assertIn('openminds:', query)
        self.assertIn('schema:', query)
        self.assertIn('FILTER', query)
        self.assertIn('LIMIT', query)
    
    def test_authentication_class(self):
        """Test authentication class structure"""
        from minds_sparql_tutorial import EBRAINSAuthenticator
        
        auth = EBRAINSAuthenticator()
        self.assertIsNone(auth.token)
        self.assertIsNone(auth.client)
        
        # Test with fake token
        auth.token = "fake_token"
        self.assertEqual(auth.token, "fake_token")

class TestDataProcessing(unittest.TestCase):
    """Test data processing and visualization functions"""
    
    def test_demo_data_creation(self):
        """Test that demo data is created correctly"""
        # This would test the create_demo_data function
        demo_data = {
            'species': pd.DataFrame({
                'Species': ['Homo sapiens', 'Mus musculus'],
                'Count': [45, 78],
                'Percentage': [25.3, 43.8]
            })
        }
        
        self.assertIsInstance(demo_data['species'], pd.DataFrame)
        self.assertEqual(len(demo_data['species']), 2)
        self.assertIn('Species', demo_data['species'].columns)
    
    def test_query_result_processing(self):
        """Test processing of query results"""
        raw_sparql_results = {
            'results': {
                'bindings': [
                    {
                        'dataset': {'value': 'http://example.com/dataset1'},
                        'name': {'value': 'Test Dataset 1'}
                    },
                    {
                        'dataset': {'value': 'http://example.com/dataset2'},
                        'name': {'value': 'Test Dataset 2'}
                    }
                ]
            }
        }
        
        # Test the _process_sparql_results method
        from minds_sparql_tutorial import MindsDataQuerier, EBRAINSAuthenticator
        
        auth = EBRAINSAuthenticator()
        querier = MindsDataQuerier(auth)
        
        results = querier._process_sparql_results(raw_sparql_results)
        
        self.assertEqual(len(results), 2)
        self.assertIn('dataset', results[0])
        self.assertIn('name', results[0])

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
