from flask import Flask, render_template
import datetime as dt


app = Flask(__name__)


@app.route("/")
def home():
    current_date = dt.datetime.now().strftime("%B %d, %Y")
    return render_template("index.html", current_date=current_date)


if __name__ == "__main__":
    app.run(debug=True)