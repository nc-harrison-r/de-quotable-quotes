from src.s3_tasks import write_file_to_s3, read_file_from_s3
from moto import mock_aws
import boto3
import pytest
import os
from unittest.mock import patch, mock_open

test_file_contents = """Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date;
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimm'd;
And every fair from fair sometime declines,
By chance or nature's changing course untrimm'd;
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow'st;
Nor shall death brag thou wander'st in his shade,
When in eternal lines to time thou grow'st:
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee."""


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope="function")
def aws(aws_credentials):
    with mock_aws():
        yield


@pytest.fixture(scope="function")
def s3_with_bucket(aws):
    s3 = boto3.client("s3")
    s3.create_bucket(
        Bucket="test_bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    yield s3


@pytest.fixture(scope="function")
def s3_bucket_with_file(aws):
    s3 = boto3.client("s3")
    s3.create_bucket(
        Bucket="test_bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    s3.put_object(Bucket="test_bucket", Key="poem.txt", Body=test_file_contents)
    yield s3


@pytest.mark.it(
    "unit test: write_file_to_s3 returns success message when bucket exists"
    " - file added to bucket"
)
def test_write_file_to_s3_returns_success_message(s3_with_bucket):
    assert (
        write_file_to_s3(
            s3_with_bucket, "tests/sonnet18.txt", "test_bucket", "poem.txt"
        )
        == "Successfully added file to bucket"
    )

    assert (
        boto3.client("s3")
        .get_object(Bucket="test_bucket", Key="poem.txt")["Body"]
        .read()
        .decode()
        == test_file_contents
    )


@pytest.mark.it(
    "unit test: write_file_to_s3 returns error message if put_object "
    "operation is unsuccessful"
)
def test_write_file_to_s3_error_message(aws):
    s3 = boto3.client("s3")
    assert "Client Error:" in write_file_to_s3(
        s3, "tests/sonnet18.txt", "test_bucket", "poem.txt"
    )


# Note: Could probably do with a test for handling file io errors


@pytest.mark.it(
    "unit test: read_file_from_s3 reads file from s3 and returns "
    "success message - local file saved"
)
def test_read_file_from_s3_success(s3_bucket_with_file):
    with patch("builtins.open", mock_open()) as m:
        assert (
            read_file_from_s3(
                s3_bucket_with_file, "test_bucket", "poem.txt", "temp.txt"
            )
            == "File read successfully"
        )

        m.assert_called_once_with("temp.txt", "w")
        handle = m()
        handle.write.assert_called_once_with(test_file_contents)


@pytest.mark.it(
    "unit test: read_file_from_s3 return error message if get_object "
    "operation is unsuccessful"
)
def test_read_file_from_s3_handles_aws_error(s3_with_bucket):
    assert "Client Error:" in read_file_from_s3(
        s3_with_bucket, "tests/sonnet18.txt", "test_bucket", "poem.txt"
    )


# Note: Could probably do with a test for handling file io errors
