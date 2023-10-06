class formulas:
    def energy(inputs):
        sum = 0
        # loop through inputs and check for key to calculate
        for (key, value) in inputs.items():
            if key == 'electricBill':
                sum = value * 0.0005 * 12
            elif key == 'gasBill':
                sum += value * 0.0053 * 12
            elif key == 'fuelBill':
                sum += value * 2.32 * 12
        return round(sum, 2)

    def waste(inputs):
        sum = 0
        for (key, value) in inputs.items():
            if key == 'totalWaste':
                sum += value * 12
            elif key == 'recyclePercentage':
                sum = sum * (0.57 - (value / 100))
        return round(sum, 2)

    def businessTravel(inputs):
        sum = 0
        for (key, value) in inputs.items():
            if key == 'kmsTravelled':
                sum += value * 2.31
            elif key == 'fuelEfficiency':
                sum = sum / value
        return round(sum, 2)
