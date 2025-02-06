from flask import Flask, render_template, request

app = Flask(__name__)

# Store spending limits and expenses
spending_limits = {}
expenses = {}

@app.route("/", methods=["GET", "POST"])
def home():
    global spending_limits, expenses  # Ensure we modify global dictionaries

    if request.method == "POST":
        action = request.form.get("action")

        # If user is setting a new spending limit
        if action == "set_limit":
            category = request.form.get("category").lower()
            new_limit = float(request.form.get("new_limit", 0))
            spending_limits[category] = new_limit  # Set limit
            expenses[category] = 0  # Initialize expense for this category

        # If user is adding an expense
        e
