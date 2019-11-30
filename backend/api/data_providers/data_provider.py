from abc import ABC, abstractmethod
from typing import List, Dict

import requests


class DataProvider(ABC):
    @abstractmethod
    def get_overview(self, session: requests.Session) -> List[Dict]:
        pass

    @abstractmethod
    def get_grade_data(self, session: requests.Session, course_id: int) -> List[Dict]:
        pass
