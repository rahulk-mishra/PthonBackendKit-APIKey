from collections.abc import MutableMapping
from .request import SDK_VERSION
import base64
import json
import requests
from .exception import APIException
from .simpleLogger import SimpleLogger

log = SimpleLogger(False)


def flatten(dictionary, parent_key=False, join_with='.'):
    items = []
    for key, value in dictionary.items():
        new_key = str(parent_key) + join_with + key if parent_key else key
        if isinstance(value, MutableMapping):
            if not value.items():
                items.append((new_key,None))
            else:
                items.extend(flatten(value, new_key, join_with).items())
        else:
            items.append((new_key, value))
    return dict(items)


def requestHeaders(request_options):
    default_headers = {
            'version': request_options.api_version, 
            'User-Agent' : SDK_VERSION,
            'x-merchantid' : request_options.merchant_id,
            'x-customerid' : request_options.customer_id
            }
    inp_headers = request_options.custom_headers
    default_headers = getAuthorizationValueWithoutPassword(request_options, default_headers)
    if inp_headers is not None:
        for k,v in default_headers.items():
            if k not in inp_headers:
                inp_headers[k]=v
        return inp_headers
    else:
        return default_headers
    
def getAuthorizationValueWithoutPassword(request_options, default_headers):
    if request_options.api_key is not None:
        apikey = base64.b64encode(request_options.api_key.encode('utf-8')).decode('utf-8')
        default_headers["Authorization"] = "Basic {}".format(apikey)
    return default_headers


def makeServiceCall(method, route, parameter, content_type, request_type):
    try:
        req_headers = requestHeaders(request_type)
        response = request(method, route, parameter, content_type, request_type, req_headers)
        return response
    except Exception as e:
        # raise APIException("-1","connection_error","connection_error", "Invalid Auth  ---" + str(e))
        log.error(str(e))
        raise APIException("-1", "connection_error","connection_error", str(e))
    
def request(method, route, parameters, content_type, request_type, req_headers):
    try:
        url = request_type.base_url + route
        response = makeRequest(url, method.upper(), parameters, req_headers, content_type, request_type.timeout)
        result = handle_response(response)
        return result
    except IOError as err:
        raise APIException("-1","connection_error","connection_error", err)
    

def makeRequest(url, method, parameters, req_headers, content_type, timeout):
    if method == 'GET':
        return requests.get(url, headers = req_headers, params=parameters, timeout=timeout)
    elif method == 'POST':
        if content_type == "application/json":
            res = requests.post(url, headers = req_headers, json=parameters, timeout=timeout)
            return res
        else: 
            input_json = flatten(parameters)
            return requests.post(url, headers = req_headers, data=input_json, timeout=timeout)
    else: 
        raise APIException(error_message="Method not supported")
        
def handle_response(response):
    if response.status_code >= 200 and response.status_code < 300:
        return response.json()
    else :
        if response.content is not None or len(response.content)!=0:  
            my_bytes_value = response.content.decode().replace("'", '"')
            if len(my_bytes_value)!=0:
                res = json.loads(my_bytes_value)
                status = res.get('status')
                error_code = res.get('error_code')
                error_message = res.get('error_message')
                if response.status_code in [400,404]:
                    raise APIException(response.status_code, status, error_code, error_message)
                elif response.status_code == 401:
                    raise APIException(response.status_code, status, error_code, error_message)
                else:
                    raise APIException(response.status_code, "internal_error" , "internal_error", "Something went wrong.")
            else :
                raise APIException(response.status_code, "internal_error" , "internal_error", "Something went wrong.")
        
