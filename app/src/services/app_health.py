import boto3
from botocore.config import Config
import logging

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    # retries = {
    #     'max_attempts': 1,
    #     'mode': 'standard'
    # }
)


def check_aws_connection():
    # TODO: implement real call to aws describe instances. If successful, return true. otherwise return False
    #return True
    ec2 = boto3.client('ec2', config=my_config)
    try:
        response = ec2.describe_instances()
        if response['Reservations']:
         return True
    except Exception as e:
        logging.exception(e)
        return False

def check_db_connection():
    # TODO: implement real select query to db. If successful, return true. otherwise return False
    return True


def is_app_healthy(healthchecks):
    return all([check["Value"] for check in healthchecks])


def get_app_health():
    health_checks = [
        {"Name": "aws-connection", "Value": check_aws_connection()},
        {"Name": "db-connection", "Value": check_db_connection()},
    ]

    return health_checks, is_app_healthy(health_checks)
