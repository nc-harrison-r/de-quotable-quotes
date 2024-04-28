# The DE Quote Engine

These tasks are designed to help you practice using the `boto3` library
which can be used to access the AWS API through Python. It is also important
that you get used to using the `moto` library for testing AWS infrastructure.

## Set-Up
1. Fork and clone this repo.
2. Run:
  ```bash
  make requirements
  make dev-setup
  ```
This will set up the virtual environment and install all the required 
dependencies.

3. Set up the following environment variables, putting in your own preferred values
  as required:
  ```bash
  TF_VAR_DDB_TABLE_NAME=<INSERT DESIRED DYNAMODB TABLE NAME>
  TF_VAR_STREAM_NAME=<INSERT DESIRED KINESIS STREAM NAME>
  TF_VAR_S3_BUCKET_PREFIX=<INSERT DESIRED S3 BUCKET NAME PREFIX>
  ```
4. Make sure you have AWS credentials in place. Then, change to the `terraform`
 directory and run:
  ```bash
  terraform init
  terraform plan
  terraform apply
  ```
  The Terraform code in this repo should be complete and requires no further work.
  It will create an S3 bucket, a [DynamoDB](https://aws.amazon.com/dynamodb/) table, 
  and a [Kinesis](https://aws.amazon.com/kinesis/) message stream. It 
  will store the names of these entities in the [AWS Systems Manager](https://aws.amazon.com/systems-manager/) Parameter Store.

You can use `make unit-test` to run unit tests or `make run-checks` to run all tests including
linting and security.
  
## Tasks
### Task One
In the `src` directory, the file `helpers_task_1.py` contains a function called
`get_parameter`. This function should retrieve parameters from the SSM Parameter 
Store. Implement the function, testing it properly using the `moto` library. You
may change the function signature if you need to.

### Task Two
The file `s3_task_2.py` contains functions called `write_file_to_s3` and 
`read_file_from_s3`. Implement these functions, testing them properly with 
the `moto` library. Again, you may change the function signature if you need to.
When you are finished, you should be able to run `python src/s3_task_2.py` and the
code will write a file to the real S3 bucket you created.

### Task Three
The file `dynamodb_task_3.py` contains functions called `put_quote_in_db` and 
`get_quotes_by_author_from_db`. Implement these functions, testing them 
properly with the `moto` library. You may change the function signature if you 
need to. When you are finished, you should be able to run 
`python src/dynamodb_task_3.py` and the code will write a quote to the real table you
created. 

The record should be in the format `Author (String), QuoteId (String), Content (String)`.
To make a  unique `QuoteId`, you may find the `uuid` built-in library useful.

### Task Four
The file `kinesis_task_4.py` contains functions called 
`write_quote_record_to_stream` and `get_quotes_from_stream`. Implement these 
functions, testing them properly with the `moto` library. You may change the 
function signature if you need to. When you are finished, you should be able to run 
`python src/kinesis_task_4.py` and the code will write a quote to the real stream you created.
  