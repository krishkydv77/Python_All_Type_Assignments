# --------------------------------------------
# Personal Finance & Data Analyzer
# Developed by: Krishan Kumar Yadav
# --------------------------------------------

transactions = []
financial_year = int(input("Enter financial year: "))


# Add Transaction

def add_transaction():
    print("\nAdd Transaction")
    t_type = input("Enter type (income/expense): ").strip().upper()

    if t_type not in ["INCOME", "EXPENSE"]:
        print("Invalid type!")
        return

    category = input("Enter category: ").strip().upper()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Bhai only digit")
        return
    
    try:
        day = int(input("Enter day (1-31): "))
        month = int(input("Enter month (1-12): "))
        year = financial_year
    except ValueError:
        print("Invalid date hai  (Bhai digit/number type)")
        return

    transaction = {"type": t_type,"category": category,"amount": amount,"day": day,"month": month,"year": year}

    transactions.append(transaction)
    print(" Bhadai ho! Transaction added successfully!")


'''
Calculate Overall Summary
'''
def calculate_summary():
    total_income = 0
    total_expense = 0

    for t in transactions:
        if t["type"] == "INCOME":
            total_income += t["amount"]
        else:
            total_expense += t["amount"]

    savings = total_income - total_expense

    print("\n----- Overall Financial Summary -----")
    print("Total Income :", total_income)
    print("Total Expense:", total_expense)
    print("Net Savings  :", savings)

    return total_income, total_expense, savings



# Monthly Analysis

def monthly_analysis():
    try:
        A_month = int(input("Enter month (1-12): "))
        A_year = int(input("Enter year: "))
    except ValueError:
        print("digit type kar bhai .... ")
        return

    total_income = 0
    total_expense = 0

    for t in transactions:
        if t["month"] == A_month and t["year"] == A_year:
            if t["type"] == "INCOME":
                total_income += t["amount"]
            else:
                total_expense += t["amount"]

    savings = total_income - total_expense

    print("\n----- Monthly Analysis -----")
    print("Total Income :", total_income)
    print("Total Expense:", total_expense)
    print("Savings      :", savings)



# Category Analysis

def category_analysis():
    category_totals = {}

    for t in transactions:
        if t["type"] == "EXPENSE":
            cat = t["category"]
            amount=t["amount"]
            if cat in category_totals:
                category_totals[cat] += amount
            else:
                category_totals[cat]= amount

    if not category_totals:
        print("\nNo expense data available.")
        return

    print("\n----- Category Analysis -----")

    total_expense = sum(category_totals.values())

    for cat, amount in category_totals.items():
         
        if total_expense > 0:
            percentage = (amount / total_expense) * 100
        else: 
            percentage=0
        print(f"{cat} : {amount} ({percentage:.2f}%)")

    
    highest_category = ""
    highest_amount = 0

    for cat in category_totals:
        if category_totals[cat] > highest_amount:
            highest_amount = category_totals[cat]
            highest_category = cat
    print("Highest Spending Category:", highest_category)


# View Transactions

def view_transactions():
    if not transactions:
        print("\n No transactions found.")
        return

    print("\n----- All Transactions -----")

    i = 1
    for t in transactions:
        print(f"{i}. {t['type']} | {t['category']} | {t['amount']} | "
              f"{t['day']}-{t['month']}-{t['year']}")
        i += 1


# Main Menu

def show_menu():
    while True:
        print("\n====== Personal Finance & Data Analyzer ======")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Overall Financial Summary")
        print("4. Category Analysis")
        print("5. Monthly Analysis")
        print("6. Exit")

        choice = input("Select option (1-6): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            calculate_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            monthly_analysis()
        elif choice == "6":
            print("Exiting Program. Thank You!")
            break
        else:
            print("Invalid choice!")


show_menu()