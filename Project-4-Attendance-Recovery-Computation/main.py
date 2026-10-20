print("ATTENDANCE RECOVERY COMPUTATION")
total = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))
required = float(input("Enter required attendance percentage: "))

if total <= 0 or attended < 0 or attended > total or required <= 0 or required > 100:
    print("Invalid input.")
else:
    current = attended / total * 100
    future = 0
    while (attended + future) / (total + future) * 100 < required:
        future = future + 1
    print("Current Attendance:", round(current, 2), "%")
    if future == 0:
        print("You already meet the attendance requirement.")
    else:
        print("Minimum consecutive classes to attend:", future)
        print("Projected Attendance:", round((attended + future) / (total + future) * 100, 2), "%")