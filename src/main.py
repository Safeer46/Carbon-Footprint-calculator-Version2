from middleware.calculators import calculators
from middleware.helper import helper


def main():
    # load choices for the user
    choice = helper.selectionOfCalculator()

    # run calculator based on choice 
    if choice == 'Energy':
        print("You have selected Energy Calculator\n")
        energyCalculation = calculators.energy()
        print("Your energy based carbon emission is: ", energyCalculation, " KgCO2")
    elif choice == 'Waste':
        print("You have selected Waste Calculator\n")
        wasteCalculation = calculators.waste()
        print("Your waste based carbon emission is: ", wasteCalculation, " KgCO2")

    elif choice == 'Business Travel':
        print("you have selected travelled kms\n")
        businessTravel = calculators.businessTravel()
        print("your kms travelled emission is:", businessTravel, "kgCO2")

    elif choice == "All":
        print("You have selected the Universal Calculations\n")
        all = calculators.all()


if __name__ == "__main__":
    main()
