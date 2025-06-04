import requests
import json

# get_access_token() obtains a token to access the Mayo Apigee APIs.
def get_access_token():
    client_id = "enter client id here" 
    secret_id = "enter secret id here"

    apigee_url = "https://internal.mcc.api.mayo.edu/oauth/token"

    payload = f'grant_type=client_credentials&client_id={client_id}&client_secret={secret_id}'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", apigee_url, headers=headers, data=payload)

    access_token_str = json.loads(response.text)
    access_token = access_token_str["access_token"]
    return access_token

# call_gpt_with_prompt() prompts GPT-4 using the token obtained by get_access_token(). 
def call_gpt_with_prompt(system_content, user_content, apigee_token):
    gpt_version = 'gpt-4'
    api_version = '2023-05-15' # Replace with your version
    
    endpoint_payload = {
        "messages": [
            {
                "role": "system",
                "content": system_content, 
            },
            {
                "role": "user",
                "content": user_content,
            }
        ],
        "temperature": 0,
        "top_p": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }

    apigee_url = 'https://internal.mcc.api.mayo.edu'
    api_openai_url = apigee_url + f"/ai-factory-product-build-azure-openai/openai/deployments/{gpt_version}/chat/completions?api-version={api_version}"
    headers = {'Authorization': f'Bearer {apigee_token}'}

    response = requests.request("POST", api_openai_url, headers=headers, json=endpoint_payload)
    json_object = json.loads(response.text)
    if "error" in json_object:
        return "invalid response"
    
    # This if statement extracts and returns the content of GPT-4's response 
    if ("choices" in json_object and len(json_object["choices"]) > 0 and "content" in json_object["choices"][0]["message"]):
        return json_object["choices"][0]["message"]["content"]
    return "invalid response"