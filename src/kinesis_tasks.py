from src.helpers_tasks import get_quote, get_parameter

STREAM_NAME = get_parameter("/temp/sprint/kinesis/stream_name")


def write_quote_record_to_stream(
  quote: dict, stream_name: str = STREAM_NAME, **kwargs
):
    """Writes a quote to a stream.

    Given a stream name and a quote, writes the quote to the stream,
    serialised as JSON.

    Args:
      quote: a quote in the format produced by the get_quote helper function.
      stream_name: the name of a Kinesis stream.
      (optional) kwargs

    Returns:
      A string indicating success or a helpful error message.
    """
    # implement me
    pass


def get_quotes_from_stream(stream_name, **kwargs):
    """Reads the latest quotes from a stream.

    Given a stream name, reads the most recent quotes from the stream.

    Args:
      stream_name: the name of a Kinesis stream.
      (optional) kwargs

    Returns:
      A stringified list of quotes or a helpful error message.
    """
    # implement me
    pass


if __name__ == "__main__":
    status, result = get_quote()
    if status == 200:
        msg = write_quote_record_to_stream(result)
        print(msg)
    else:
        print(result["status_message"])
