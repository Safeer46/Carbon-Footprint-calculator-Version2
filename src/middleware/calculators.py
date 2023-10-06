from middleware.helper import helper
from middleware.formulas import formulas


class calculators:
    def energy():
        inputs = {'electricBill': 0.00, 'gasBill': 0.00, 'fuelBill': 0.00}

        # change texts
        inputs['electricBill'] = helper.validateFloat("\nAvg Monthly Electricity bill:")
        inputs['gasBill'] = helper.validateFloat("Avg Monthly Gas bill:")
        inputs['fuelBill'] = helper.validateFloat("Avg Monthly Fuel bill:")

        # calculate with formula
        calculatedResponse = formulas.energy(inputs)

        return calculatedResponse

    def waste():
        inputs = {'totalWaste': 0.00, 'recyclePercentage': 0.00}
        inputs['totalWaste'] = helper.validateFloat("\nAvg Monthly total waste:")
        inputs['recyclePercentage'] = helper.validateFloat("\nAvg Monthly recycle percentage:")

        calculatedResponse = formulas.waste(inputs)
        return calculatedResponse

    def businessTravel():
        inputs = {'kmsTravelled': 0.00, 'fuelEfficiency': 0.00}
        inputs['kmsTravelled'] = helper.validateFloat("\nAvg travelled kms per year:")
        inputs['fuelEfficiency'] = helper.validateFloat("\nAvg fuel efficiency of the car:")

        calculatedResponse = formulas.businessTravel(inputs)
        return calculatedResponse

    def all():
        energy = calculators.energy()
        print("Your energy based carbon emission is: ", energy, " KgCO2")

        waste = calculators.waste()
        print("Your waste based carbon emission is: ", waste, " KgCO2")

        businessTravel = calculators.businessTravel()
        print("Your Business travel based carbon emission is:", businessTravel, " KgCO2")
        return "Thank you for using our calculator!"
