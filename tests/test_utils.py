import unittest
import pandas as pd
from utils import load_data  # Assuming load_data is in a utils.py file
from unittest.mock import MagicMock
import sys

# Mock streamlit for tests
sys.modules["streamlit"] = MagicMock()
class TestUtils(unittest.TestCase):
    def setUp(self):
        # Test setup: Mock dataset paths or create dummy datasets
        self.benin_data = pd.DataFrame({
            "Timestamp": ["2023-01-01 00:00", "2023-01-01 01:00"],
            "GHI": [100, 200],
            "DNI": [150, 250],
            "DHI": [50, 100],
            "Tamb": [30, 35],
            "TModA": [25, 30],
            "TModB": [20, 25],
            "WS": [2.5, 3.0],
            "RH": [50, 55]
        })

        self.sierra_leone_data = pd.DataFrame(self.benin_data)
        self.togo_data = pd.DataFrame(self.benin_data)

    def test_load_data(self):
        # Test that load_data function returns dataframes
        # Mocking actual file reads here; replace with mocks in practice
        benin_data, sierra_leone_data, togo_data = load_data()
        self.assertIsInstance(benin_data, pd.DataFrame)
        self.assertIsInstance(sierra_leone_data, pd.DataFrame)
        self.assertIsInstance(togo_data, pd.DataFrame)

    def test_data_columns(self):
        # Ensure dataframes have expected columns
        expected_columns = [
            "Timestamp", "GHI", "DNI", "DHI", "Tamb", "TModA", "TModB", "WS", "RH"
        ]
        benin_data, _, _ = load_data()
        self.assertTrue(set(expected_columns).issubset(benin_data.columns))

if __name__ == "__main__":
    unittest.main()
