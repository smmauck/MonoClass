import requests

from .data_provider import DataProvider


class CanvasDataProvider(DataProvider):
    session: requests.Session = None

    def __init__(self, session: requests.Session):
        self.session = session

    def get_class_data(self):
        pass

    def get_grade_data(self):
        pass
