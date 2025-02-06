from flask import Flask, render_template, request

app = Flask(__name__)  # Create Flask app

# Define spending limits and expenses globally
spending_limits = {"food": 500, "shopping": 300, "entertainment": 200, "transport": 150}
expenses = {"food": 0, "shopping": 0, "entertainment": 0, "transport": 0}

@app.route("/", methods=["GET", "POST"])  # Homepage route
def home():
    if request.method == "POST":
        # Handle the form submission to add expense
        category = request.form.get("category")
        amount = float(request.form.get("amount", 0))
        if category in expenses:
            expenses[category] += amount  # Add expense to the category
        
    return render_template("index.html", spending_limits=spending_limits, expenses=expenses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Required for Render
