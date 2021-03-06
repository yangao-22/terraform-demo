terraform {
  required_version = ">=0.12.0"
}

provider "aws" {
  version = "~> 2.0"
  region  = "us-east-1"
  access_key = "***"
  secret_key = "******"
}

module "lambda_archive" {
  source      = "./terraform-aws-lambda-src-archive"
  src_dir     = "./tictactoe"
  output_path = "./artifacts/tictactoe.zip"
}

#data "archive_file" "src" {
#  type        = "zip"
#  source_file = "${path.module}/src/start.rb"
#  output_path = "${path.module}/artifacts/src.zip"
#}
