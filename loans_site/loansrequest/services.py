import requests
import os


class MoniClient:
    _ROOT_ENDPOINT = "https://api.moni.com.ar/api/v4/scoring/pre-score/"
    _CRED = os.getenv("API_PASS")
    _HEADER = {"credential": f"{_CRED}"}


    def validate_loan(self, dni) -> bool:
        endpoint = f"{self._ROOT_ENDPOINT}{dni}"
        appr = requests.get(url=endpoint, headers=self._HEADER)
        if appr.json()['status']=='approve':
            return True
        return False


moni_client = MoniClient()