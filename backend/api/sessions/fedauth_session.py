import requests
from pyquery import PyQuery as pq

from .base_session import BaseSession
from api.login_behaviors import CanvasLoginBehavior, MoodleLoginBehavior


class FedauthSession(BaseSession):
    session = requests.Session()

    def __init__(self):
        self.register_login_behavior(CanvasLoginBehavior())
        self.register_login_behavior(MoodleLoginBehavior())

    def _base_login(self, username: str, password: str) -> None:
        self.session.get("http://mycuinfo.colorado.edu/")

        parser = pq(
            self.session.get(
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

        res = self.session.post("https://fedauth.colorado.edu/idp/profile/SAML2/POST/SSO", data=payload)

        payload = {
            "timezoneOffset": 0,
            "j_username": username,
            "j_password": password,
            "_eventId_proceed": "Log In"
        }

        res = self.session.post(res.url, data=payload)

        # Incorrect credentials
        if "Set-Cookie" not in res.headers:
            self.session = None
