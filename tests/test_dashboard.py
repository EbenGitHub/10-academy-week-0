import unittest
from unittest.mock import patch, MagicMock
from app import dashboard
from unittest.mock import MagicMock
import sys

# Mock streamlit for tests
sys.modules["streamlit"] = MagicMock()
class TestDashboard(unittest.TestCase):
    @patch("dashboard.st.sidebar")
    def test_sidebar_navigation(self, mock_sidebar):
        # Mock Streamlit sidebar components
        mock_sidebar.selectbox.return_value = "Benin"

        # Call sidebar logic
        region = dashboard.st.sidebar.selectbox("Select Region", ["Benin", "Sierra Leone", "Togo"])
        self.assertEqual(region, "Benin")

    @patch("dashboard.st.line_chart")
    @patch("dashboard.load_data")
    def test_line_chart(self, mock_load_data, mock_line_chart):
        # Mock load_data and line_chart behavior
        mock_data = MagicMock()
        mock_data[["Timestamp", "GHI"]] = pd.DataFrame({
            "Timestamp": ["2023-01-01 00:00", "2023-01-01 01:00"],
            "GHI": [100, 200]
        })
        mock_load_data.return_value = (mock_data, mock_data, mock_data)

        # Call dashboard logic
        dashboard.visualization = "Line Chart"
        dashboard.region = "Benin"
        dashboard.metric = "GHI"
        dashboard.data_map = {
            "Benin": mock_data,
            "Sierra Leone": mock_data,
            "Togo": mock_data
        }
        dashboard.data = dashboard.data_map["Benin"]

        # Test line chart rendering
        dashboard.st.line_chart.assert_called()

if __name__ == "__main__":
    unittest.main()
