import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILENAME = "expenses.csv"
BUDGET_FILE = "budget.txt"

def log_expense():
    expense = pd.DataFrame([{
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Category": input("Category: "),
        "Amount": float(input("Amount: ")),
        "Description": input("Description: ")
    }])

    try:
        df = pd.read_csv(FILENAME)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

    df = pd.concat([df, expense], ignore_index=True)
    df.to_csv(FILENAME, index=False)
    print("Expense added!")

def view_expenses():
    try:
        df = pd.read_csv(FILENAME)
        if df.empty:
            print("No expenses yet.")
        else:
            print(df.to_string(index=False))
    except FileNotFoundError:
        print("No file found.")

def show_summary():
    try:
        df = pd.read_csv(FILENAME)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Week"] = df["Date"].dt.isocalendar().week
        df["Month"] = df["Date"].dt.month_name()
        print("\n--- Monthly Summary ---")
        print(df.groupby("Month")["Amount"].sum())
        print("\n--- Weekly Summary ---")
        print(df.groupby("Week")["Amount"].sum())
    except:
        print("No data to summarize.")

def plot_chart():
    try:
        df = pd.read_csv(FILENAME)
        cat_sum = df.groupby("Category")["Amount"].sum()
        cat_sum.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
        plt.title("Spending by Category")
        plt.ylabel("")
        plt.show()
    except:
        print("No data to plot.")

def set_budget():
    budget = float(input("Set your monthly budget: ₹"))
    with open(BUDGET_FILE, "w") as f:
        f.write(str(budget))
    print("Budget saved.")

def check_overspending():
    if not os.path.exists(FILENAME) or not os.path.exists(BUDGET_FILE):
        print("Add expenses and set a budget first.")
        return

    df = pd.read_csv(FILENAME)
    df["Date"] = pd.to_datetime(df["Date"])
    this_month = datetime.now().month
    month_expenses = df[df["Date"].dt.month == this_month]["Amount"].sum()

    with open(BUDGET_FILE, "r") as f:
        budget = float(f.read())

    print(f"This month’s expenses: ₹{month_expenses:.2f}")
    print(f"Budget: ₹{budget:.2f}")
    if month_expenses > budget:
        print("You’ve overspent this month!")

def menu():
    while True:
        print("\n===== Expense Tracker (pandas) =====")
        print("1. Log Expense")
        print("2. View All Expenses")
        print("3. Show Summary (Monthly/Weekly)")
        print("4. Show Spending Chart")
        print("5. Set Monthly Budget")
        print("6. Check Overspending Alert")
        print("7. Export as CSV (auto)")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")
        if choice == "1": log_expense()
        elif choice == "2": view_expenses()
        elif choice == "3": show_summary()
        elif choice == "4": plot_chart()
        elif choice == "5": set_budget()
        elif choice == "6": check_overspending()
        elif choice == "7": print("Data already saved as CSV.")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()

