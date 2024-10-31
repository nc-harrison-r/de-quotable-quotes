from boto3 import client
from src.helpers_tasks import get_quote, get_parameter

PARAMETER_NAME = "/temp/sprint/kinesis/stream_name"


def write_quote_record_to_stream(k_client, quote, stream_name):
    """Writes a quote to a stream.

    Given a stream name and a quote, writes the quote to the stream, serialised as JSON.

    Args:
      quote: a quote in the format produced by the get_quote helper function.
      stream_name: the name of a Kinesis stream.
      (optional) kwargs

    Returns:
      A string indicating success or a helpful error message.
    """
    # implement me
    pass


def get_quotes_from_stream(k_client, stream_name):
    """Reads the latest quotes from a stream.

    Given a stream name, reads the most recent quotes from the stream.

    Args:
      k_client: a boto3 client for Kinesis.
      stream_name: the name of a Kinesis stream.
      (optional) kwargs

    Returns:
      A stringified list of quotes or a helpful error message.
    """
    # implement me
    pass


if __name__ == "__main__":
    ssm_client = client("ssm")
    STREAM_NAME = get_parameter(ssm_client, PARAMETER_NAME)

    status, result = get_quote()
    if status == 200:
        k_client = client("kinesis")
        msg = write_quote_record_to_stream(k_client, result, STREAM_NAME)
        print(f"==>> msg: {msg}")
        stream = get_quotes_from_stream(k_client, STREAM_NAME)
        print(f"==>> stream: {stream}")
    else:
        print(result["status_message"])
