#!/usr/bin/env python3
"""Module parameterizes a unit test"""

from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """Class parameterizes a unit test"""

    @parameterized.expand([
        ({"a": 1}, 'a', 1),
        ({"a": {"b": 2}}, 'a', {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Method parameterizes a unit test"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """an instance that mocks and patches a unittest"""
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """method mocks and patches a unittest"""
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
            mock_get.reset_mock()
