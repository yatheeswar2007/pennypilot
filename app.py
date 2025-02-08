from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize spending limits and expenses
spending_limits = {}
expenses = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "set_limit":
            category = request.form.get("category")
            new_limit = request.form.get("new_limit")

            if category and new_limit:
                spending_limits[category.lower()] = float(new_limit)
                expenses[category.lower()] = 0  # Initialize category expense

        elif action == "remove_category":
            category = request.form.get("category")

            if category in spending_limits:
                del spending_limits[category]  # Remove limit
                del expenses[category]  # Remove expenses

    return render_template("index.html", spending_limits=spending_limits, expenses=expenses)

@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        category = request.form.get("category")
        amount = request.form.get("amount")

        if category and amount:
            category = category.lower()
            if category in expenses:
                expenses[category] += float(amount)
        
        return redirect(url_for("home"))  # Redirect to home after adding an expense

    return render_template("add_expense.html", spending_limits=spending_limits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
