from botocore.exceptions import ClientError
from boto3 import client
from src.helpers_tasks import get_parameter

PARAMETER_NAME = "/temp/sprint/s3/bucket_name"


def write_file_to_s3(s3_client, path_to_file, bucket_name, object_key, **kwargs):
    """Writes a file to the given S3 bucket.

    Given a path to local file, writes the file to the given S3 bucket and key.

    Args:
      s3_client: a boto3 client to interact with the AWS S3 API.
      path_to_file: a local file path, either absolute or relative to the root
                    of this repository.
      bucket_name: name of the bucket to write to.
      object_key: intended key of the object within the bucket.
      (optional) kwargs

    Returns:
      A string indicating success or an informative error message.

    """
    # implement me
    try:
        with open(path_to_file) as f:
            file_contents = "".join(line for line in f)
            s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=file_contents)
        return "Successfully added file to bucket"
    except ClientError as c:
        return f"Client Error: {c}"
    except Exception:
        raise


def read_file_from_s3(s3_client, bucket_name, object_key, destination, **kwargs):
    """Reads a file from the given S3 bucket.

    Given a bucket name and key, reads the file to the given local destination.

    Args:
      s3_client: a boto3 client to interact with the AWS API.
      bucket_name: name of the bucket to read from.
      object_key: key of the object within the bucket.
      destination: a local file path, either absolute or relative to the root of this repository.
      (optional) kwargs

    Returns:
      A string indicating success or an informative error message.

    """
    # implement me
    pass


if __name__ == "__main__":
    ssm_client = client("ssm")
    s3_bucket_name = get_parameter(ssm_client, PARAMETER_NAME)

    s3_client = client("s3")
    msg = write_file_to_s3(
        s3_client, "tests/sonnet18.txt", s3_bucket_name, "sonnets/sonnet18.txt"
    )
    print(msg)

    file = read_file_from_s3(
        s3_client, s3_bucket_name, "sonnets/sonnet18.txt", "sonnet18.txt"
    )
    print(file)
