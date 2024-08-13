import pytest
from unittest.mock import patch
from src.helpers_tasks import get_quote, get_parameter


class TestGetQuote:
    """Tests the get_quote helper."""

    def test_get_quote_returns_status_and_formatted_dict(
        self, sample_quote_list, result_quote_1
    ):
        with patch("src.helpers_tasks.random.choice") as mock_choice:
            mock_choice.return_value = sample_quote_list[0]
            assert get_quote() == (200, result_quote_1)

    def test_get_quote_valid_url(self):
        status_code, _ = get_quote()
        assert status_code == 200

    def test_get_quote_error_response(self):
        with patch(
            "src.helpers_tasks.random.choice",
            side_effect=Exception("The requested resource could not be found"),
        ):
            status_code, response = get_quote()
            assert status_code == 500
            assert response == {
                "status_message": (
                    "Unexpected error: The requested resource could not be found"
                )
            }
