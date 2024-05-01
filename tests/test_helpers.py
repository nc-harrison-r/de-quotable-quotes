import pytest
from requests import Response
from unittest.mock import Mock, patch
from src.helpers_tasks import get_quote, URL, get_parameter


class TestGetQuote:
    """Tests the get_quote helper."""

    @pytest.mark.it("unit test: get_quote returns correctly formatted dict")
    def test_get_quote_dict(self, sample_quote_list, result_quote_1):
        mock_response = Mock(spec=Response, status_code=200)
        with patch("src.helpers_task_1.requests.get") as mock_request:
            mock_request.return_value = mock_response
            mock_response.json.return_value = sample_quote_list[0:1]
            assert get_quote() == (200, result_quote_1)

    @pytest.mark.it("unit test: get_quote calls correct url")
    def test_get_quote_url(self):
        with patch("src.helpers_task_1.requests.get") as mock_request:
            get_quote()
            mock_request.assert_called_once_with(URL)

    @pytest.mark.it("integration test: get_quote gets valid url")
    def test_get_quote_valid_url(self):
        status_code, _ = get_quote()
        assert status_code == 200

    @pytest.mark.it("unit test: returns correct message if non 200 response")
    def test_get_quote_error_response(self):
        status_code, response = get_quote(url="https://api.quotable.io/quotes/wibble")
        assert status_code == 404
        assert response == {
            "status_message": "The requested resource could not be found"
        }
