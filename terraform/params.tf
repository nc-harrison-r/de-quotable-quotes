resource "aws_ssm_parameter" "bucket_name" {
  name = "/temp/sprint/s3/bucket_name"
  type = "String"
  value = aws_s3_bucket.testing_bucket.id
}

resource "aws_ssm_parameter" "dynamo_db_table" {
  name = "/temp/sprint/dynamodb/table_name"
  type = "String"
  value = aws_dynamodb_table.quote_table.name
}

resource "aws_ssm_parameter" "stream_name" {
  name = "/temp/sprint/kinesis/stream_name"
  type = "String"
  value = aws_kinesis_stream.quote_stream.name 
}