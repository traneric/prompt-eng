import requests
import json
import os
import time

def load_config():
    with open('config', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
    return

def create_payload(model, prompt, **kwargs):
    payload = {
        "model": model,
        "prompt": prompt, 
        "stream": False,
    }

    if kwargs:
        payload["options"] = {key: value for key, value in kwargs.items()}
    
    return payload


def model_req(payload):
    # CUT-SHORT Condition
    try:
        load_config()
    except:
        return 0, f"!!ERROR!! Problem loading CONFIG"

    url = os.getenv('URL', None)
    api_key = os.getenv('API_KEY', None)
    result = delta = response = None

    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer API_KEY"

    # Send out request to Model Provider
    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        delta = time.time() - start_time
    except:
        result = f"!!ERROR!! Request failed! Have you setup the URL and API_KEY properly ({url})?"

    # Checking the response and extracting the 'response' field
    if response and response.status_code == 200:
        result = response.json().get('response', 'No response field found')
    elif response:
        result = f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"
    
    return round(delta,3), result
