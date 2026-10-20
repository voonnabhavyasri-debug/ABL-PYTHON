print("FOOD WASTE MONITORING SYSTEM")
items = int(input("Enter number of food items: "))
if items <= 0:
    print("Invalid item count.")
else:
    total_prepared = 0.0
    total_wasted = 0.0
    valid = True
    for i in range(items):
        print("Food item", i + 1)
        prepared = float(input("Prepared quantity in kg: "))
        wasted = float(input("Wasted quantity in kg: "))
        if prepared < 0 or wasted < 0 or wasted > prepared:
            valid = False
        total_prepared = total_prepared + prepared
        total_wasted = total_wasted + wasted
    if not valid:
        print("Invalid quantities. Wasted quantity must be between 0 and prepared quantity.")
    elif total_prepared == 0:
        print("No food was prepared.")
    else:
        percentage = total_wasted / total_prepared * 100
        print("Total food prepared:", round(total_prepared, 2), "kg")
        print("Total food wasted:", round(total_wasted, 2), "kg")
        print("Waste percentage:", round(percentage, 2), "%")
        if percentage > 20:
            print("Waste level: High")
        else:
            print("Waste level: Within Target")