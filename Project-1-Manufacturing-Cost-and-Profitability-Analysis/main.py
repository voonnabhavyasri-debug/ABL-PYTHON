print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")
print("---------------------------------------------")

units = int(input("Enter number of units produced: "))
material = float(input("Enter material cost per unit: "))
labour = float(input("Enter labour cost per unit: "))
wastage = float(input("Enter total wastage cost: "))
machine = float(input("Enter total machine cost: "))
selling_price = float(input("Enter selling price per unit: "))
target = float(input("Enter target profit: "))

if (units <= 0 or material < 0 or labour < 0
        or wastage < 0 or machine < 0
        or selling_price < 0 or target < 0):
    print("Invalid input. Enter valid values.")
else:
    material_cost = units * material
    labour_cost = units * labour

    total_cost = material_cost + labour_cost + wastage + machine
    revenue = units * selling_price
    profit = revenue - total_cost
    cost_per_unit = total_cost / units

    print("\n----- PRODUCTION REPORT -----")
    print("Total Material Cost:", material_cost)
    print("Total Labour Cost:", labour_cost)
    print("Total Wastage Cost:", wastage)
    print("Total Machine Cost:", machine)
    print("Total Production Cost:", total_cost)
    print("Cost Per Unit:", round(cost_per_unit, 2))
    print("Total Sales Revenue:", revenue)
    print("Total Profit:", profit)

    if profit >= target:
        print("Profit Target Achieved")
    else:
        print("Profit Target Not Achieved")
