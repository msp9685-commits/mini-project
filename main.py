from flask import request, render_template, Flask, redirect
import json

app = Flask(__name__)
expenses = []
@app.route("/", methods = ["GET", "POST"])
def add_expense():
    expenses = load_expenses()
    if request.method == "POST":
        expense = request.form.get("expense")
        description = request.form.get("describe")
        expenses.append({"amount":expense, "description": description})
        save_expenses(expenses)
        return redirect("/")
    total = 0
    for expense in expenses:
        total += int(expense["amount"])
    return render_template("index.html", expenses=expenses, total=total)
@app.route("/delete", methods = ["GET", "POST"])
def del_expense():
    expenses = load_expenses()
    if request.method == "POST":
        index = int(request.form.get("index"))
        expenses.pop(index)
        save_expenses(expenses)
    return redirect ("/")
@app.route("/edit", methods = ["POST"])
def edit_expense():
    expenses = load_expenses()
    if request.method == "POST":
        index = int(request.form.get("index"))
        new_expense = request.form.get("expense")
        new_description = request.form.get("describe")
        expenses[index]= ({"amount":new_expense, "description": new_description})
        save_expenses(expenses)
    return redirect("/")
def load_expenses():
    with open("expenses.json", "r") as file:
        return json.load(file)
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
app.run(debug=True)