import requests
from pyquery import PyQuery as pq

from .login_behavior import LoginBehavior


class MoodleLoginBehavior(LoginBehavior):
    def login(self, session: requests.Session) -> None:
        session.get("https://moodle.cs.colorado.edu/")

        parser = pq(session.get("https://moodle.cs.colorado.edu/auth/shibboleth/index.php").content)

        relay_state = parser("input").eq(0).attr("value")
        saml_response = parser("input").eq(1).attr("value")

        payload = {
            "RelayState": relay_state,
            "SAMLResponse": saml_response,
        }

        session.post("https://moodle.cs.colorado.edu/Shibboleth.sso/SAML2/POST", data=payload)
