def initialize_tracker(initial_balance):
    return {
        'balance': initial_balance,
        'expenses': []
    }

def add_expense(tracker, amount, description):
    tracker['balance'] -= amount
    tracker['expenses'].append((amount, description))

def view_balance(tracker):
    return tracker['balance']

def view_expenses(tracker):
    return tracker['expenses']

def track_expenses():
    expense_tracker = initialize_tracker(3000)


    add_expense(expense_tracker, 60, "Groceries")
    add_expense(expense_tracker, 30, "Dinner")
    add_expense(expense_tracker, 1200, "Movie")

