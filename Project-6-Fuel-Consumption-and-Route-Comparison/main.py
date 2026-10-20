print("FUEL CONSUMPTION AND ROUTE COMPARISON")
distance_a = float(input("Enter Route A distance in km: "))
distance_b = float(input("Enter Route B distance in km: "))
efficiency = float(input("Enter vehicle efficiency in km per litre: "))
price = float(input("Enter fuel price per litre: "))
if distance_a < 0 or distance_b < 0 or efficiency <= 0 or price < 0:
    print("Invalid input.")
else:
    litres_a = distance_a / efficiency
    litres_b = distance_b / efficiency
    cost_a = litres_a * price
    cost_b = litres_b * price
    print("Route A fuel required:", round(litres_a, 2), "litres")
    print("Route A fuel cost:", round(cost_a, 2))
    print("Route B fuel required:", round(litres_b, 2), "litres")
    print("Route B fuel cost:", round(cost_b, 2))
    if cost_a < cost_b:
        print("Route A has the lower estimated fuel cost.")
    elif cost_b < cost_a:
        print("Route B has the lower estimated fuel cost.")
    else:
        print("Both routes have equal estimated fuel cost.")