from flask import Flask, request, render_template
import string

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def return_statement():
    string_to_test = request.form['text']
    # print(string_to_test)
    alphabet = set(string.ascii_lowercase)

    lowered_string = set(string_to_test.lower())

    # print(lowered_string.issuperset(alphabet))
    return str(lowered_string.issuperset(alphabet))
