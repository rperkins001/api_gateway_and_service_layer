import requests
from config.api_config import API_CONFIG
from ..service_layer import (
    customer_example_function,
    jira_example_function,
    dns_example_function,
)

FUNCTION_MAP = {
    'customer_tickets': {
        'example_function': customer_example_function,
    },
    'jira_tickets': {
        'example_function': jira_example_function,
    },
    'dns': {
        'example_function': dns_example_function,
    },
}


class APIWallService:
    def __init__(self):
        self.base_url = API_CONFIG['api_wall']['base_url']
        self.headers = {"Authorization": f"Bearer {API_CONFIG['api_wall']['api_key']}"}

    def fetch_data_from_source(self, source):
        url = f"{self.base_url}/{source}/data"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data from {source}: {response.status_code} {response.text}")

    def send_data_to_source(self, source, data):
        url = f"{self.base_url}/{source}/update"
        response = requests.post(url, headers=self.headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error sending data to {source}: {response.status_code} {response.text}")
        
    def execute_api_function(self, source, function_name, data=None):
        if source in FUNCTION_MAP and function_name in FUNCTION_MAP[source]:
            func = FUNCTION_MAP[source][function_name]
            return func(data)
        else:
            raise Exception(f"Unknown source '{source}' or function '{function_name}'")
