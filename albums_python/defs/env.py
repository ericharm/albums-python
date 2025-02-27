import os

ENV = os.environ["ENV"]
ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"]

IS_PRODUCTION = ENV == "production"
