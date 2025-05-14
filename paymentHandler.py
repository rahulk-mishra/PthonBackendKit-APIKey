from utils.exception import APIException
from utils import client
from utils.request import Request
    
class PaymentHandler:
    def __init__(self, merchant_id, base_url, auth, customer_id = None, timeout=None, api_version=None):
        self.request = Request(merchant_id, base_url, auth, customer_id, timeout, api_version)
        pass  

    def validate_params(self, params):
        if not isinstance(params, dict):
            raise APIException(
                -1,
                "INVALID_PARAMS",
                "INVALID_PARAMS",
                "Params are empty or not an object"
            )
        
    def session(self, params):
        self.validate_params(params)
        path = "/session"
        method = 'POST'
        response = client.makeServiceCall(method, path, params, "application/json", self.request)
        return response
    
    
    def order_status(self, params):
        order_id = None
        if isinstance(params, str):
            order_id = params
        else:
            self.validate_params(params)
            order_id = params.get("order_id")

        if order_id is None:
            raise APIException(
                -1,
                "INVALID_PARAMS",
                "INVALID_PARAMS",
                "order_id is missing, usage:- order_status('order_id') or order_status({'order_id': 'value', ...other configs here})"
            )
        
        path = f"/orders/{order_id}"
        method = "GET"

        response = client.makeServiceCall(method, path, params, "application/json", self.request)
        return response
    
    def refund(self, params):
        order_id = None
        if isinstance(params, str):
            order_id = params
        else:
            self.validate_params(params)
            order_id = params.get("order_id")

        if order_id is None:
            raise APIException(
                -1,
                "INVALID_PARAMS",
                "INVALID_PARAMS",
                "order_id is missing, usage:- refund('order_id)"
            )
        
        method = 'POST'
        path = f"/orders/{order_id}/refunds"
        response = client.makeServiceCall(method, path, params, "application/json", self.request)
        return response


    