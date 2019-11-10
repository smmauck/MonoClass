import requests
from pyquery import PyQuery as pq

from .login_behavior import LoginBehavior


class CanvasLoginBehavior(LoginBehavior):
    def login(self, session: requests.Session) -> None:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3",
        }

        parser = pq(session.get("https://canvas.colorado.edu/", headers=headers).content)

        saml_response = parser("input").eq(0).attr("value")

        payload = {
            "SAMLResponse": saml_response
        }

        session.post("https://canvas.colorado.edu/login/saml", data=payload)
