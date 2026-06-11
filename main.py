from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    url_curta = None

    if request.method == "POST":

        url = request.form["url"]

        try:
            encurtador = pyshorteners.Shortener()
            url_curta = encurtador.tinyurl.short(url)

        except Exception:
            url_curta = "Erro ao encurtar a URL."

    return render_template("index.html", url_curta=url_curta)


if __name__ == "__main__":
    app.run(debug=True)