# Helper class will allow us to reuse the functions
class helper:
    def validateFloat(prompt):

        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def selectionOfCalculator():
        print("\nSelect the calculation(s) you want to perform:\na. Energy Consumed")
        print("b. Waste Emissions")
        print("c. Business Travel")
        print("d. All")
        print("e. Exit")
        listOfCalculators = {'a': "Energy", 'b': "Waste", 'c': "Business Travel", 'd': "All", 'e': "Exit"}
        choice = input("Enter your choice (a, b, c, d, or e): ")
        while True:
            try:
                if choice == 'e':
                    print("Thank you for using the Carbon Calculator!\n")
                    exit()
                elif choice in listOfCalculators:
                    return listOfCalculators[choice]
                else:
                    print("Invalid selection. Please enter a valid option.")
                    choice = input("Enter your choice (a, b, c, d, or e): ")
            except ValueError:
                print("Invalid selection. Please enter a valid option.")
