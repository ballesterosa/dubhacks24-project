import requests
import os
from dotenv import load_dotenv

load_dotenv()
YOUR_API_KEY = os.getenv("API_KEY")

url = "https://api.perplexity.ai/chat/completions"

def payload_function(
          symptoms:str='No symptoms were entered.'
        , doctor_diagnosis:str='No doctor diagnosis enterred'
        , tests_run:str='No tests run'
        , additional_info:str='No tests run'
    ):
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user. The user"
                "will provide medical information and you will respond with validation of the"
                "information provided. The user will input their symptoms, diagnosis, test, and more"
                "and you will determine if any other diagnosis, information, or outcomes should be"
                "considered and if the actions taken thus far were appropriate."
            },
            {
                "role": "user",
                "content": f'Symptoms: {symptoms}, \n'
                f'Doctor Diagnosis: {doctor_diagnosis}, \n'
                f'Tests Run: {tests_run}, \n'
                f'Additional information: {additional_info}'
            }
        ],
        "max_tokens": None,
        "temperature": 0.2,
        "top_p": 0.9,
        "return_citations": True,
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
    return payload

payload = payload_function(
      symptoms='yellow eyes, yellow scela'
    , doctor_diagnosis='jaundice'
    , additional_info='symptoms present for past 7 days, family history of diabetes')
headers = {
    "Authorization": f'Bearer {YOUR_API_KEY}',
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

with open('output.txt', 'w') as file:
    file.write(response.text.choices.message.content)