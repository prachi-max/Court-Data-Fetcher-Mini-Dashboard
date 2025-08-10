from flask import Flask, render_template, request
from scraper import fetch_case_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        case_year = request.form["case_year"]

        # Fetch the result HTML from the scraper
        result_html = fetch_case_data(case_type, case_number, case_year)

        # Pass HTML to result.html
        return render_template("result.html", result=result_html)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
