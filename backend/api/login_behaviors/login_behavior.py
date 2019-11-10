from abc import ABC, abstractmethod

import requests


class LoginBehavior(ABC):
    @abstractmethod
    def login(self, session: requests.Session) -> None:
        pass
