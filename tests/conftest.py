import pytest
from moto import mock_aws
import os
import boto3
import json


@pytest.fixture(scope="module")
def sample_quote_list():
    return [
        {
            "_id": "KBBVyoNtUib6",
            "content": "Most great people have attained their greatest success ",
            "author": "Napoleon Hill",
            "tags": ["Success"],
            "authorSlug": "napoleon-hill",
            "length": 99,
            "dateAdded": "2020-01-15",
            "dateModified": "2023-04-14",
        },
        {
            "_id": "UQ2TjZ5IIDSR",
            "content": "Anyone who doesn't take truth seriously in small matters.",
            "author": "Albert Einstein",
            "tags": ["Famous Quotes"],
            "authorSlug": "albert-einstein",
            "length": 96,
            "dateAdded": "2020-02-22",
            "dateModified": "2023-04-14",
        },
        {
            "_id": "iqob_h7AuhiT",
            "content": "Only through our connectedness to others can we really know.",
            "author": "Harriet Lerner",
            "tags": ["Famous Quotes"],
            "authorSlug": "harriet-lerner",
            "length": 171,
            "dateAdded": "2020-01-26",
            "dateModified": "2023-04-14",
        },
    ]


@pytest.fixture(scope="module")
def result_quote_1():
    return {
        "content": "Most great people have attained their greatest success ",
        "author": "Napoleon Hill",
        "length": 99,
    }


@pytest.fixture(scope="module")
def result_quote_2():
    return {
        "content": "Anyone who doesn't take truth seriously in small matters.",
        "author": "Albert Einstein",
        "length": 96,
    }


@pytest.fixture(scope="module")
def result_quote_3():
    return {
        "content": "Only through our connectedness to others can we really know.",
        "author": "Harriet Lerner",
        "length": 171,
    }
