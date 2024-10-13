import requests
import os
from dotenv import load_dotenv

load_dotenv()
YOUR_API_KEY = os.getenv("API_KEY")

url = "https://api.perplexity.ai/chat/completions"

def payload_function(
    patient_info: str = 'No patient information provided'
  , symptoms: str = 'No symptoms provided'
  , medical_history: str = 'No medical history provided'
  , doctor_actions: str = 'No doctor actions provided'
  , additional_info: str = 'No additional information provided'
):
    payload = {
        "model": "llama-3.1-sonar-small-128k-online"
      , "messages": [
            {
                "role": "system"
              , "content": "You are an advanced medical analysis AI assistant designed to enhance patient safety "
                "and diagnostic accuracy. Your task is to analyze patient-provided information, including "
                "demographics, symptoms, medical history, doctor's actions, and additional context. Based on "
                "this data, you will:\n\n"
                "1. Evaluate the appropriateness and completeness of the current diagnosis and treatment plan.\n"
                "2. Identify any potential oversights or missed diagnoses that should be considered.\n"
                "3. Suggest additional tests or examinations that might be beneficial.\n"
                "4. Compare the provided information with up-to-date medical knowledge.\n"
                "5. Highlight any discrepancies or areas of concern that may require further attention.\n"
                "6. Provide a comprehensive analysis to assist healthcare providers.\n\n"
                "Your goal is to serve as a supplementary tool to improve patient care, potentially uncovering "
                "overlooked diagnoses or treatment options. Always advise patients to consult with their "
                "healthcare providers regarding any concerns or suggestions you identify."
            }
          , {
                "role": "user"
              , "content": f"Patient Information:\n{patient_info}\n\n"
                f"Symptoms:\n{symptoms}\n\n"
                f"Medical History:\n{medical_history}\n\n"
                f"Doctor's Actions (diagnosis, tests, treatments):\n{doctor_actions}\n\n"
                f"Additional Information:\n{additional_info}\n\n"
                f"Based on this information, please provide a comprehensive analysis of the patient's condition, "
                f"evaluate the current diagnosis and treatment, suggest any additional considerations or potential "
                f"diagnoses that may have been overlooked, and recommend any further tests or examinations that "
                f"might be beneficial. Interpret and categorize the provided information as needed."
            }
        ]
      , "max_tokens": None
      , "temperature": 0.2
      , "top_p": 0.9
      , "return_citations": True
      , "search_domain_filter": ["perplexity.ai"]
      , "return_images": False
      , "return_related_questions": False
      , "search_recency_filter": "month"
      , "top_k": 0
      , "stream": False
      , "presence_penalty": 0
      , "frequency_penalty": 1
    }
    return payload

# def payload_function(
#           symptoms:str='No symptoms were entered.'
#         , doctor_diagnosis:str='No doctor diagnosis enterred'
#         , tests_run:str='No tests run'
#         , additional_info:str='No additional information'
#     ):
#     payload = {
#         "model": "llama-3.1-sonar-small-128k-online",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": "You are an artificial intelligence assistant and you need to "
#                 "engage in a helpful, detailed, polite conversation with a user. The user"
#                 "will provide medical information and you will respond with validation of the"
#                 "information provided. The user will input their symptoms, diagnosis, test, and more"
#                 "and you will determine if any other diagnosis, information, or outcomes should be"
#                 "considered and if the actions taken thus far were appropriate."
#             },
#             {
#                 "role": "user",
#                 "content": f'Symptoms: {symptoms}, \n'
#                 f'Doctor Diagnosis: {doctor_diagnosis}, \n'
#                 f'Tests Run: {tests_run}, \n'
#                 f'Additional information: {additional_info}'
#             }
#         ],
#         "max_tokens": None,
#         "temperature": 0.2,
#         "top_p": 0.9,
#         "return_citations": True,
#         "search_domain_filter": ["perplexity.ai"],
#         "return_images": False,
#         "return_related_questions": False,
#         "search_recency_filter": "month",
#         "top_k": 0,
#         "stream": False,
#         "presence_penalty": 0,
#         "frequency_penalty": 1
#     }
#     return payload

payload = payload_function(
    patient_info='20 year old, male, caucasian, student'
    , symptoms='yellow eyes, yellow scela'
    , medical_history='diabetes'
    , doctor_actions='jaundice'
    , additional_info='symptoms present for past 7 days, family history of diabetes')
headers = {
    "Authorization": f'Bearer {YOUR_API_KEY}',
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

with open('output.txt', 'w') as file:
    file.write(response.text)