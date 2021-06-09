import os
import unittest
from runner import Runner

MODULE_NAME = "e2e"
RESOURCE_TYPE = "aws_vpc.this"

class TestE2E(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.snippet = """
        provider "aws" {
              access_key                  = "test"
              region                      = "us-east-1"
              s3_force_path_style         = true
              secret_key                  = "test"
              skip_credentials_validation = true
              skip_metadata_api_check     = true
              skip_requesting_account_id  = true
              endpoints {
                apigateway     = "http://localstack:4567"
                cloudformation = "http://localstack:4581"
                cloudwatch     = "http://localstack:4582"
                dynamodb       = "http://localstack:4569"
                ec2            = "http://localstack:4597"
                es             = "http://localstack:4578"
                firehose       = "http://localstack:4573"
                iam            = "http://localstack:4593"
                kinesis        = "http://localstack:4568"
                lambda         = "http://localstack:4574"
                route53        = "http://localstack:4580"
                redshift       = "http://localstack:4577"
                s3             = "http://localstack:4572"
                secretsmanager = "http://localstack:4584"
                ses            = "http://localstack:4579"
                sns            = "http://localstack:4575"
                sqs            = "http://localstack:4576"
                ssm            = "http://localstack:4583"
                stepfunctions  = "http://localstack:4585"
                sts            = "http://localstack:4592"
              }
            }

            module "e2e" {
              source = "./mymodule"
              providers = {
                aws = aws
              }
            }
        """

        self.runner = Runner(self.snippet)
        self.result = self.runner.result

    def test_vpc_cidr(self):
        self.assertEqual(self.runner.get_value(f"module.{MODULE_NAME}.{RESOURCE_TYPE}", "cidr_block"), "10.0.0.0/16")

if __name__ == '__main__':
    unittest.main()
