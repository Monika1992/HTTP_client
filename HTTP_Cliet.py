from bs4 import BeautifulSoup as bs
from requests import *


class HTTP_Client(object):

    def __init__(self, config_instance, logger_instance, FTP_client):
        self.config = config_instance
        self.logger = logger_instance
        self.FTP_client = FTP_client

    def test_http_connection(self, http_address):
        pass

    def get_http_data(self, http_connection):
        pass

    def kill_http(self):
        pass