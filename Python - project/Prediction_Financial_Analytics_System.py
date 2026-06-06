# ================== DATA STORAGE 
records = []


# ================== VALIDATION + ADD RECORD 
def add_record():
    try:
        month = int(input("Enter Month (1-12): "))
        year = int(input("Enter Year: "))
        income = float(input("Enter Income: "))
        expense = float(input("Enter Expense: "))
    except ValueError:
        print("Invalid input! Numbers only.")
        return

    if month < 1 or month > 12:
        print("Invalid month!")
        return

    if income < 0 or expense < 0:
        print("Income/Expense cannot be negative!")
        return

    records.append({
        "month": month,
        "year": year,
        "income": income,
        "expense": expense
    })

    print("Record Added Successfully.")


# ================== VIEW RECORDS 
def view_records():
    if not records:
        print("No records available.")
        return

    print("\n----- Records -----")
    i = 1
    for r in records:
        print(i, "|", r["month"], "/", r["year"],
              "| Income:", r["income"],
              "| Expense:", r["expense"])
        i += 1


# ================== OVERALL SUMMARY 
def overall_summary():
    if not records:
        print("No records available.")
        return

    total_income = 0
    total_expense = 0

    for r in records:
        total_income += r["income"]
        total_expense += r["expense"]

    savings = total_income - total_expense

    print("\n----- Overall Summary -----")
    print("Total Income   :", round(total_income, 2))
    print("Total Expense  :", round(total_expense, 2))
    print("Total Savings  :", round(savings, 2))

    if total_income > 0:
        ratio = (savings / total_income) * 100
        print("Saving Ratio   :", round(ratio, 2), "%")


# ================== GROWTH RATE 
def calculate_growth(expense_list):
    if len(expense_list) < 2:
        return 0

    first = expense_list[0]
    last = expense_list[-1]

    if first == 0:
        return 0

    return ((last - first) / first) * 100


# ================== MULTI-HORIZON ANALYSIS 
def multi_horizon_analysis(window):
    if len(records) < window:
        print("Not enough data.")
        return

    expense_list = []
    for r in records[-window:]:
        expense_list.append(r["expense"])

    total = 0
    for e in expense_list:
        total += e

    avg = total / window

    print(f"\nLast {window} Month Average Expense:", round(avg, 2))

    growth = calculate_growth(expense_list)
    print("Growth Rate (%):", round(growth, 2))


# ================== FORECAST ENGINE (HYBRID)
def forecast(window, months_ahead):
    if len(records) < window:
        print("Not enough data for forecast.")
        return

    expense_list = []
    for r in records[-window:]:
        expense_list.append(r["expense"])

    # Moving Average
    total = 0
    for e in expense_list:
        total += e
    moving_avg = total / window

    # Trend
    first = expense_list[0]
    last = expense_list[-1]
    trend = (last - first) / (window - 1)

    print("\n----- Forecast -----")

    for i in range(1, months_ahead + 1):
        prediction = moving_avg + (i * trend)

        if prediction < 0:
            prediction = 0

        print("Month", i, "Prediction:", round(prediction, 2))

    # Confidence
    if len(records) < 6:
        confidence = "Low"
    elif len(records) < 12:
        confidence = "Medium"
    else:
        confidence = "High"

    print("Forecast Confidence:", confidence)


# ================== FINANCIAL HEALTH 
def financial_health():
    if not records:
        print("No data available.")
        return

    last = records[-1]
    income = last["income"]
    expense = last["expense"]

    if income == 0:
        print("Cannot calculate health.")
        return

    saving_ratio = ((income - expense) / income) * 100

    print("Saving Ratio:", round(saving_ratio, 2), "%")

    if saving_ratio > 30:
        print("Status: Healthy")
    elif saving_ratio >= 20:
        print("Status: Moderate")
    else:
        print("Status: Risk")


#  MENU SYSTEM 
def show_menu():
    running = True

    while running:
        print("\n===== Expense Prediction System =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Overall Summary")
        print("4. Multi-Horizon Analysis (3M)")
        print("5. Multi-Horizon Analysis (6M)")
        print("6. Forecast Next Month (3M)")
        print("7. Forecast Next 6 Months (6M)")
        print("8. Financial Health Score")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            overall_summary()
        elif choice == "4":
            multi_horizon_analysis(3)
        elif choice == "5":
            multi_horizon_analysis(6)
        elif choice == "6":
            forecast(3, 1)
        elif choice == "7":
            forecast(6, 6)
        elif choice == "8":
            financial_health()
        elif choice == "9":
            running = False
        else:
            print("Invalid choice!")



show_menu()