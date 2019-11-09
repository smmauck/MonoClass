from abc import ABC, abstractmethod
from typing import Union

import requests
from pyquery import PyQuery as pq


class DataProvider(ABC):
    @property
    @abstractmethod
    def session(self):
        pass

    @staticmethod
    def base_login(username: str, password: str) -> Union[requests.Session, None]:
        s = requests.session()
        s.get("http://mycuinfo.colorado.edu/")

        parser = pq(
            s.get(
                "https://ping.prod.cu.edu/idp/startSSO.ping?PartnerSpId=SP:EnterprisePortal&IdpSelectorId=BoulderIDP"
                "&TargetResource=https://portal.prod.cu.edu%2Fpsp%2Fepprod%2FUCB2%2FENTP%2Fh%2F%3Ftab%3DDEFAULT"
            ).content
        )

        saml_request = parser("input").eq(0).attr("value")
        relay_state = parser("input").eq(1).attr("value")

        payload = {
            "SAMLRequest": saml_request,
            "RelayState": relay_state
        }

        res = s.post("https://fedauth.colorado.edu/idp/profile/SAML2/POST/SSO", data=payload)

        payload = {
            "timezoneOffset": 0,
            "j_username": username,
            "j_password": password,
            "_eventId_proceed": "Log In"
        }

        res = s.post(res.url, data=payload)

        # Correct credentials
        if "Set-Cookie" in res.headers:
            return s
        else:
            return None

    @abstractmethod
    def get_class_data(self):
        pass

    @abstractmethod
    def get_grade_data(self):
        pass
