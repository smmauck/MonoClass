from abc import ABC, abstractmethod
from typing import Union, List

import requests

from api.login_behaviors import LoginBehavior


class BaseSession(ABC):
    additional_login_behaviors: List[LoginBehavior] = []

    @property
    @abstractmethod
    def session(self):
        pass

    @abstractmethod
    def _base_login(self, username: str, password: str) -> None:
        pass

    def login(self, username: str, password: str) -> Union[requests.Session, None]:
        self._base_login(username, password)

        if self.session is None:
            return self.session
        else:
            self.__finalize_login()
            return self.session

    def register_login_behavior(self, login_behavior: LoginBehavior):
        self.additional_login_behaviors.append(login_behavior)

    def __finalize_login(self):
        for login_behavior in self.additional_login_behaviors:
            login_behavior.login(self.session)
