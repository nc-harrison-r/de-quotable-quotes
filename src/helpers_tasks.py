import requests

URL = "https://api.quotable.io/quotes/random"


def get_quote(url: str = URL):
    """Gets quote from external API.

    Calls the quotable.io API for a random quote, retrieving both the
    author and the text of the quote.

    Args:
      (optional) url: the URL of the API. Default value provided.

    Returns:
      (On success) a tuple consisting of the HTTP status code and a dict
      containing the content, author and length of the quote as keys.
      (On failure) a tuple with the status code and a dict containing the
      status message.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw = response.json()
        required = ["content", "author", "length"]
        return (response.status_code, {k: raw[0][k] for k in required})
    except requests.HTTPError:
        formatted = {"status_message": response.json()["statusMessage"]}
        return (response.status_code, formatted)


def get_parameter(parameter_name: str, **kwargs):
    """Gets a parameter from AWS Systems Manager Parameter Store.

    Finds the given parameter name in the Parameter store and returns the
    value.

    Args:
      parameter_name: the unique name of the parameter.
      (optional) kwargs

    Returns:
      A string with the required parameter value or an informative error
      message.

    """
    # implement me
    pass
