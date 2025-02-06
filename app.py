from flask import Flask, render_template

app = Flask(__name__)  # Create Flask app

@app.route("/")  # Homepage route
def home():
    return render_template("index.html")  # Load HTML file

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Required for Render
    spending_limits = {"food": 500, "shopping": 300, "entertainment": 200, "transport": 150}
expenses = {"food": 0, "shopping": 0, "entertainment": 0, "transport": 0}

