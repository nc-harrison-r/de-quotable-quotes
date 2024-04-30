from src.helpers_tasks import get_parameter

PARAMETER_NAME = "/temp/sprint/s3/bucket_name"
S3_BUCKET_NAME = get_parameter(PARAMETER_NAME)


def write_file_to_s3(
  path_to_file: str, bucket_name: str, object_key: str, **kwargs
):
    """Writes a file to the given S3 bucket.

    Given a path to local file, writes the file to the given S3 bucket and key.

    Args:
      path_to_file: a local file path, either absolute or relative to the root
                    of this repository.
      bucket_name: name of the bucket to write to.
      object_key: intended key of the object within the bucket.
      (optional) kwargs

    Returns:
      A string indicating success or an informative error message.

    """
    # implement me
    pass


def read_file_from_s3(bucket_name, object_key, destination, **kwargs):
    """Reads a file from the given S3 bucket.

    Given a bucket name and key, reads the file to the given local destination.

    Args:
      bucket_name: name of the bucket to read from.
      object_key: key of the object within the bucket.
      destination: a local file path, either absolute or relative to the root
      of this repository.
      (optional) kwargs

    Returns:
      A string indicating success or an informative error message.

    """
    # implement me
    pass


if __name__ == "__main__":
    msg = write_file_to_s3(
      "tests/sonnet18.txt", S3_BUCKET_NAME, "sonnets/sonnet18.txt")
    print(msg)
