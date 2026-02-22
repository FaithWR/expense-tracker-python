import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    expenses = load_expenses()
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    total = 0
    print("\n--- Expenses ---")
    for expense in expenses:
        print(f"{expense['name']} - {expense['amount']}")
        total += expense["amount"]
    print(f"\nTotal Expenses: {total}")

def main():
    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()