import pytest
from unittest.mock import patch
from src.helpers_tasks import get_quote, get_parameter, NotAnSSMClientError
import os
from moto import mock_aws
import boto3
from botocore.exceptions import EndpointConnectionError


@pytest.fixture(scope="function")
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope="function")
def ssm_client(aws_credentials):
    with mock_aws():
        yield boto3.client("ssm")


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


class TestGetParameter:
    """Tests the get_parameter helper."""

    def test_a_string_is_returned_from_get_parameter(self, ssm_client):
        ssm_client.put_parameter(Name="test_parameter", Value="_", Type="String")
        output = get_parameter(ssm_client, "test_parameter")
        assert isinstance(output, str)

    def test_value_returned_for_given_parameter_name(self, ssm_client):
        ssm_client.put_parameter(
            Name="test_parameter", Value="super_secret_value", Type="String"
        )
        output = get_parameter(ssm_client, "test_parameter")
        assert output == "super_secret_value"

    def test_returns_keyerror_if_parameter_name_does_not_exist(self, ssm_client):
        with pytest.raises(KeyError):
            get_parameter(ssm_client, "test_parameter")

    def test_returns_custom_error_if_ssm_client_param_is_wrong_type(self):
        with pytest.raises(NotAnSSMClientError):
            get_parameter("cheese", "_")

    # @patch("boto3.client")
    # def test_error_returned_on_no_connection(self, mock_client, aws_credentials):

    #     mock_client.get_parameter.side_effect = EndpointConnectionError(
    #         endpoint_url="https://ssm.eu-west-2.amazonaws.com"
    #     )

    #     with pytest.raises(ConnectionError):
    #         get_parameter(mock_client, "_")

        # print(f"SSM CLIENT ---> {ssm_client}")
        # print(f"PATCHY MC-PATCHFACE ---> {patch}")
