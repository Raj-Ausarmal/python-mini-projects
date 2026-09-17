print("Expense Tracker")

expenses = []

while True:
    print("\n1. Add expense")
    print("2. See expenses")
    print("3. See total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("What did you spend on? ")
        amount = float(input("How much did you spend? "))

        expenses.append([item, amount])

        print("Expense added.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added.")
        else:
            print("\nExpenses:")

            for i in range(len(expenses)):
                print(i + 1, expenses[i][0], "-", expenses[i][1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("Total spent:", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Please choose a valid option.")
