import json
from functools import lru_cache

import boto3
from mypy_boto3_ssm import SSMClient

from albums_python.domain.models.database import DatabaseCredentials


@lru_cache(maxsize=None)
def get_ssm_client() -> SSMClient:
    return boto3.client("ssm", region_name="us-east-1")


def get_albums_database_credentials() -> DatabaseCredentials:
    client = get_ssm_client()
    parameter_name = "albums-database-credentials"
    response = client.get_parameter(Name=parameter_name)
    response_value = response["Parameter"]["Value"]
    parsed_response = json.loads(response_value)
    return DatabaseCredentials(**parsed_response)
