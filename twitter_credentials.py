from dotenv import load_dotenv
import os

class TwitterInfo:
    def __init__(self):
        load_dotenv()
        self.__consumer_key = "TgcAJiraK0VYwbyHW5EO48syx"
        self.__consumer_secret = "h2EXPNGkiasULsN2iGZAhcG8fZIAXh6FTZ7zz4pSY1c6zOVghi"
        self.__access_token =  "1512334525791039490-HT6ywkJJMMcrDgxKOBzpC5oOuxNi47"
        self.__access_token_secret = "u0FuEAnX2eYM8u9Cra9p37esUSnzk31z8bqAfF4qdmIiD"

    def get_consumer_key(self):
        return self.__consumer_key

    def get_consumer_secret_key(self):
        return self.__consumer_secret

    def get_access_token_key(self):
        return self.__access_token

    def get_access_token_secret_key(self):
        return self.__access_token_secret

