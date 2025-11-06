print("Welcome to the Daily Expense Tracker!")

print()

print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []

while True:
    choice = int(input())

    if (not (1 <= choice <= 5)):
        print("Invalid choice. Please try again.")

    if choice == 1:
        flt = float(input())
        expenses.append(flt)
        print("Expense added successfully!")
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")

            cnt = 1

            for i in expenses:
                print(f"{cnt}. {i}")
                cnt += 1
    elif choice == 3:
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            ttl = 0
            avg = 0

            for i in expenses:
                ttl += i

            avg = ttl / len(expenses)

            print(f"Total expense: {ttl}")
            print(f"Average expense: {avg}")
    elif choice == 4:
        expenses.clear()
        print("All expenses cleared.")
    elif choice == 5:
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break