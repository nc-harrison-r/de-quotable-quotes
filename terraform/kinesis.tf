resource "aws_kinesis_stream" "quote_stream" {
  name = var.STREAM_NAME
  shard_count = 1
  
  stream_mode_details {
    stream_mode = "PROVISIONED"
  }
}