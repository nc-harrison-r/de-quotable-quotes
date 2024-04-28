resource "aws_dynamodb_table" "quote_table" {
  name = var.DDB_TABLE_NAME
  hash_key = "Author"
  range_key = "QuoteId"
  read_capacity = 5
  write_capacity = 5

  attribute {
    name = "Author"
    type = "S"
  }

  attribute {
    name = "QuoteId"
    type = "S"
  }

}