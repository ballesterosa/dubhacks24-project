import requests
import os
import json
import markdown
from dotenv import load_dotenv
from flask import Flask, request, render_template
from llm_api import payload_function
app = Flask(__name__)

app_params = {}
load_dotenv()
YOUR_API_KEY = os.getenv("API_KEY")
url = "https://api.perplexity.ai/chat/completions"

def results():
    payload = payload_function(
        symptoms=(app_params["symptoms"] if "symptoms" in app_params else "")
        , doctor_actions=(app_params["doc_diagnosis"] if "doc_diagnosis" in app_params else "")
        , additional_info=(app_params["doc_recomendations"] if "doc_recomendations" in app_params else "")
    )
    headers = {
        "Authorization": f'Bearer {YOUR_API_KEY}',
        "Content-Type": "application/json"
    }
    llm_response = requests.request("POST", url, json=payload, headers=headers)
    response_dict = json.loads(llm_response.text)

    return render_template("results.html", results=markdown.markdown(response_dict["choices"][0]["message"]["content"]))

@app.route('/', methods =["GET", "POST"])
def get_user_in():
    if request.method == "POST":
        # getting input with user_in = f_user_in in HTML form
        symptoms = request.form.get("f_user_in")
        went_to_doc = request.form.get("f_went_to_doc")
        doc_diagnosis = request.form.get("f_doc_diagnosis")
        doc_recomendations = request.form.get("f_doc_recommendations")
        tests_run = request.form.get("f_tests_run")


        app_params["symptoms"] = symptoms
        app_params["went_to_doc"] = went_to_doc
        app_params["doc_diagnosis"] = doc_diagnosis
        app_params["doc_recomendations"] = doc_recomendations
        app_params["tests_run"] = tests_run
        
    if "symptoms" in app_params:
        return results()
    return render_template("index.html")

