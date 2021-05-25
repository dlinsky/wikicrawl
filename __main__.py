from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from werkzeug.utils import redirect
import runner as run
from wiki_helper import WikiHelper
import os

app = Flask(__name__)


@app.route("/", methods=['POST'])
def wiki_search():
    if request.method == 'POST':
        csv = run.main(WikiHelper(), request.form["topic"], request.form["csv"], int(request.form["branch-length"]),
                       int(request.form["branch-number"]))
        htmlstr = csv.to_html(classes='table table-striped')
        pathname = os.getcwd()
        pathname = pathname + "/templates/"
        text_file = open(pathname+"csvfile.html", "w")
        text_file.write(
            "<form method=\"POST\"><input type=\"submit\" value=\"Back\"></form>")
        text_file.write(htmlstr)
        text_file.close()
        return redirect(url_for("ping", _external=1)+"csv")


@app.route("/csv", methods=['GET', 'POST'])
def csv_page():
    if request.method == 'GET':
        return render_template("csvfile.html")
    else:
        return redirect(url_for("ping", _external=1))


@app.route("/")
def ping():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
