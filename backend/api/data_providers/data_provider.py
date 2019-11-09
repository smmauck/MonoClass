from abc import ABC, abstractmethod
import requests


class DataProvider(ABC):
    @property
    @abstractmethod
    def session(self):
        pass

    @staticmethod
    def login(username: str, password: str) -> requests.Session:
        return requests.Session()

    @abstractmethod
    def get_class_data(self):
        pass

    @abstractmethod
    def get_grade_data(self):
        pass
