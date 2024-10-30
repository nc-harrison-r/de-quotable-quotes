from boto3 import client
from src.helpers_tasks import get_quote, get_parameter


def write_quote_record_to_stream(client, quote, stream_name, **kwargs):
    """Writes a quote to a stream.

    Given a stream name and a quote, writes the quote to the stream,
    serialised as JSON.

    Args:
      client: a boto3 client for Kinesis.
      quote: a quote in the format produced by the get_quote helper function.
      stream_name: the name of a Kinesis stream.
      (optional) kwargs

    Returns:
      A string indicating success or a helpful error message.
    """
    # implement me
    pass


def get_quotes_from_stream(client, stream_name, **kwargs):
    """Reads the latest quotes from a stream.

    Given a stream name, reads the most recent quotes from the stream.

    Args:
      client: a boto3 client for Kinesis.
      stream_name: the name of a Kinesis stream.
      (optional) kwargs

    Returns:
      A stringified list of quotes or a helpful error message.
    """
    # implement me
    pass


if __name__ == "__main__":
    ssm_client = client("ssm")
    STREAM_NAME = get_parameter(ssm_client, "/temp/sprint/kinesis/stream_name")

    status, result = get_quote()
    if status == 200:
        k_client = client("kinesis")
        msg = write_quote_record_to_stream(k_client, result, STREAM_NAME)
        print(msg)
    else:
        print(result["status_message"])
