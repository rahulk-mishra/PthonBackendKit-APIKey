
DEFAULT_TIMEOUT = 5 #seconds
API_VERSION = "2023-07-01"
DEFAULT_SSL_PROTOCOL = "TLSv1.2"
PROJECT_VERSION = "2023-01-01"
SDK_VERSION = 'PYTHON_SDK2/' + PROJECT_VERSION

class Request():
    def __init__(self, merchant_id, base_url, auth, customer_id = None, timeout = DEFAULT_TIMEOUT, api_version = API_VERSION):
        self.merchant_id = merchant_id
        self.base_url = base_url
        self.auth = auth
        self.customer_id = customer_id
        self.timeout = timeout
        self.api_version = api_version

        self.API_VERSION = "2023-07-01"
        self.DEFAULT_SSL_PROTOCOL = "TLSv1.2"
        self.SDK_VERSION = 'PYTHON_SDK2/1.0.0'
        
        self.auth_type = "BASIC"
        self.api_key = self.auth
        
        self.custom_headers = None
        self.query_params = None