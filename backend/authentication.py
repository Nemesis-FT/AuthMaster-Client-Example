"""
Questo modulo contiene utility di autenticazione.
"""
from social_core.backends.oauth import BaseOAuth2

class AuthMasterOAuth2(BaseOAuth2):
    name = "AuthMaster"
    API_URL = "http://127.0.0.1:8000"
    AUTHORIZATION_URL = "http://127.0.0.1:8000/oauth/authorize"
    ACCESS_TOKEN_URL = "http://127.0.0.1:8000/oauth/token"
    ACCESS_TOKEN_METHOD = "POST"
    REDIRECT_STATE = False
    DEFAULT_SCOPE = ["Profile"]
    EXTRA_DATA = [
        ("id", "id"),
        ("expires_in", "expires"),
        ("refresh_token", "refresh_token"),
    ]

    def api_url(self, path):
        api_url = self.setting("API_URL") or self.API_URL
        return "{}{}".format(api_url.rstrip("/"), path)

    def authorization_url(self):
        return self.api_url("/oauth/authorize")

    def access_token_url(self):
        return self.api_url("/oauth/token")

    def get_user_details(self, response):
        """Return user details from GitLab account"""
        return {
            "username": response.get("username") or "",
            "id": response.get("id"),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json(
            self.api_url("/api/me"), headers={"Authorization": "Bearer "+access_token}
        )
