print("CAMPUS EVENT FINANCIAL PLANNING")
venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering cost: "))
transport = float(input("Transport cost: "))
certificates = float(input("Certificate cost: "))
fee = float(input("Registration fee per participant: "))
registrations = int(input("Number of registrations: "))
sponsorship = float(input("Sponsorship amount: "))

if (venue < 0 or equipment < 0 or catering < 0 or transport < 0
        or certificates < 0 or fee < 0 or registrations < 0
        or sponsorship < 0):
    print("Invalid input. Enter non-negative values.")
else:
    total_cost = venue + equipment + catering + transport + certificates
    registration_income = fee * registrations
    total_income = registration_income + sponsorship
    balance = total_income - total_cost
    remaining_cost = total_cost - sponsorship

    print("\n----- EVENT BUDGET -----")
    print("Total Event Cost:", round(total_cost, 2))
    print("Registration Income:", round(registration_income, 2))
    print("Sponsorship:", round(sponsorship, 2))
    print("Total Available Income:", round(total_income, 2))
    print("Surplus / Shortfall:", round(balance, 2))

    if fee > 0:
        if remaining_cost <= 0:
            minimum_registrations = 0
        else:
            minimum_registrations = int(remaining_cost / fee)
            if minimum_registrations * fee < remaining_cost:
                minimum_registrations = minimum_registrations + 1
        print("Minimum Registrations to Break Even:", minimum_registrations)
    elif remaining_cost <= 0:
        print("Minimum Registrations to Break Even: 0")
    else:
        print("Break-even is not possible using registration fees alone.")
    if balance >= 0:
        print("Current budget covers the event.")
    else:
        print("Current budget has a shortfall.")