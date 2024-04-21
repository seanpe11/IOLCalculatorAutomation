import requests

def make_request_with_captcha(url, payload, headers=None):
    """
    Makes a POST request to the specified URL with a given payload.

    Args:
        url (str): The URL to which the request is made.
        payload (dict): The JSON payload to be sent in the request.
        headers (dict): Optional. Additional headers to be sent with the request.

    Returns:
        dict: The JSON response from the server.
    """
    # Default headers to use if none are provided
    if headers is None:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

# Example usage
url = "YOUR_API_ENDPOINT"
payload = {
    "os": {},
    "od": {
        "measureData": {
            "targetRefraction": -2,
            "n": 1.3375,
            "device": "ZEISS IOLMASTER 700",
            "al": 20,
            "cct": 290,
            "acd": 3,
            "wtw": 9,
            "k1": 37,
            "k2": 42,
            "k1Axis": 12,
            "k2Axis": 102,
            "lt": 4
        },
        "iolData": {
            "lensType": "Biconvex 1:1",
            "lensAConstant": 100
        },
        "calculationResult": {
            "formulaName": "Hill - RBF"
        }
    },
    "patient": {
        "patientGender": "Not provided",
        "patientId": "312",
        "patientLastname": "Sean Bean",
        "patientFirstName": "Sean"
    },
    "gRecaptchaResponse": "YOUR_VALID_gRecaptchaResponse"
}

# You'll need to replace YOUR_API_ENDPOINT with the actual endpoint you're targeting,
# and YOUR_VALID_gRecaptchaResponse with a valid CAPTCHA response token.
# Example function call (uncomment and modify the placeholder values to test):
response = make_request_with_captcha(url, payload)
print(response)

