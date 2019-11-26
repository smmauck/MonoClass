from abc import ABC, abstractmethod

import requests


class DataProvider(ABC):
    @abstractmethod
    def get_overview(self, session: requests.Session):
        pass

    @abstractmethod
    def get_grade_data(self):
        pass
