
from flask import Flask, render_template, request

app = Flask(__name__)

# Default spending limits and expenses
spending_limits = {"food": 500, "shopping": 300, "entertainment": 200, "transport": 150}
expenses = {"food": 0, "shopping": 0, "entertainment": 0, "transport": 0}

@app.route("/", methods=["GET", "POST"])
def home():
    global spending_limits  # Ensure we modify the global dictionary

    if request.method == "POST":
        action = request.form.get("action")

        # If user is adding an expense
        if action == "add_expense":
            category = request.form.get("category")
            amount = float(request.form.get("amount", 0))
            if category in expenses:
                expenses[category] += amount  # Add expense to category

        # If user is setting a new limit
        elif action == "set_limit":
            category = request.form.get("category")
            new_limit = float(request.form.get("new_limit", 0))
            if category in spending_limits:
                spending_limits[category] = new_limit  # Update the limit

    return render_template("index.html", spending_limits=spending_limits, expenses=expenses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
