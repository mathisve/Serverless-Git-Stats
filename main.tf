variable "region" {
  default = "eu-central-1"
}

provider "aws" {
  region = var.region
}

data "aws_caller_identity" "current" {}

variable "function_name" {
  default = "git-stats"
}

resource "aws_iam_role" "git_stats_lambda" {
  name = "${var.function_name}_lambda"

  assume_role_policy = <<-EOF
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  }
  EOF
}

resource "aws_lambda_function" "git_stats_lambda" {
  filename      = "archive.zip"
  description   = "Gets stats from Github.com for Mathisco-01"
  function_name = var.function_name
  role          = aws_iam_role.git_stats_lambda.arn

  handler = "main.handler"
  runtime = "python3.7"
  timeout = 5

  source_code_hash = filebase64sha256("archive.zip")
  environment {
    variables = {
      LINK = "https://github.com/users/mathisco-01/contributions"
    }
  }
}
