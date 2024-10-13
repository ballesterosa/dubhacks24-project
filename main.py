from flask import Flask, request, render_template
app = Flask(__name__)

app_params = {}

@app.route('/', methods =["GET", "POST"])
def get_user_in():
    if request.method == "POST":
        # getting input with user_in = f_user_in in HTML form
        symptoms = request.form.get("f_user_in")
        went_to_doc = request.form.get("f_went_to_doc")
        
        app_params["symptoms"] = symptoms
        app_params["went_to_doc"] = went_to_doc

        ret_text = "Symptoms: " + symptoms + "\nWent to doc: " + went_to_doc

        if went_to_doc == "yes":
            return render_template("went_to_doc.html")
        
        return ret_text
    return render_template("index.html")

def get_doc_input():
    if request.method == "POST":
        # getting input with user_in = f_user_in in HTML form
        doc_diagnosis = request.form.get("f_doc_diagnosis")
        doc_recomendations = request.form.get("f_doc_recommendations")

        app_params["doc_diagnosis"] = doc_diagnosis
        app_params["doc_recomendations"] = doc_recomendations

        ret_text = "Doc diagnosis: " + doc_diagnosis + "\nDoc recommendations: " + doc_recomendations
        return ret_text
    return render_template("index.html")