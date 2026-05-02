import requests
from typing import Optional, Dict, Any

from utils.logger import ApiLogger
logger = ApiLogger.get_logger(__name__, logfile='logs/request.log', enable_stream=False)

class HttpClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url} params={params}")
        response = self.session.get(url, params=params, headers=headers, timeout=self.timeout)
        try:
            logger.info(f"Response: {response.json()}")
        except ValueError:
            logger.info(f"Response text: {response.text}")
        return response

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, files=None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} json={json}")
        response = self.session.post(url, data=data, json=json, headers=headers, timeout=self.timeout, files=files)
        try:
            logger.info(f"Response: {response.json()}")
        except ValueError:
            logger.info(f"Response text: {response.text}")
        return response

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url} json={json}")
        response = self.session.put(url, data=data, json=json, headers=headers, timeout=self.timeout)
        try:
            logger.info(f"Response: {response.json()}")
        except ValueError:
            logger.info(f"Response text: {response.text}")
        return response

    def delete(self, endpoint: str, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url, headers=headers, timeout=self.timeout)
        try:
            logger.info(f"Response: {response.json()}")
        except ValueError:
            logger.info(f"Response text: {response.text}")
        return response