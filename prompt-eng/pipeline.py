import requests
import json
import time

def model_orch(url, payload, api_key=None):
    
    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer API_KEY"
    start_time = time.time()
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    end_time = time.time()

    # Checking the response and extracting the 'response' field
    if response.status_code == 200:
        result = response.json().get('response', 'No response field found')
        print(result)
        print(f"Time taken: {end_time - start_time:.2f} secs")
    else:
        print(f"Error: {response.status_code}, {response.text}")
