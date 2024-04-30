from src.helpers_tasks import get_parameter, get_quote


PARAMETER_NAME = "/temp/sprint/dynamodb/table_name"
TABLE_NAME = get_parameter(PARAMETER_NAME)


def put_quote_in_db(table_name: str, quote: dict, **kwargs):
    """Writes a record of a quote to a given DynamoDB table.

    Given the name of a properly-configured DynamoDB table, writes the author
    and quote to the table along with a unique ID in case an author has
    several quotes.

    The record format is Author (string), QuoteId (string), Content (string).
    The Author and Content are provided in the input quote object. The QuoteId
    must be generated within the function.

    Args:
      table_name: name of the DynamoDB table.
      quote: a quote object generated from the get_quote helper function.
      (optional) kwargs

    Returns:
      A string indicating success or an informative error message.
    """
    # implement me
    pass


def get_quotes_by_author_from_db(table_name, author, **kwargs):
    """
    Retrieves all records of quotes by a given author from the DynamoDB table.

    Given the name of a properly-configured DynamoDB table, retrieves all
    quotes by the author to a stringified list.

    Args:
      table_name: name of the DynamoDB table.
      author: name of the author.
      (optional) kwargs

    Returns:
      A string containing a list of quotes or an informative error message.
    """
    # implement me
    pass


if __name__ == "__main__":
    status, quote = get_quote()
    if status == 200:
        msg1 = put_quote_in_db(TABLE_NAME, quote)
        print(msg1)
    else:
        print(quote["status_message"])
