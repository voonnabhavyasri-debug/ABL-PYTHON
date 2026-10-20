print("STUDENT PERFORMANCE TREND ANALYSIS")
count = int(input("Enter number of assessments (minimum 2): "))
if count < 2:
    print("Please enter at least two assessments.")
else:
    marks = []
    valid = True
    for i in range(count):
        mark = float(input("Enter mark for assessment " + str(i + 1) + " (0-100): "))
        if mark < 0 or mark > 100:
            valid = False
        marks.append(mark)
    if not valid:
        print("Invalid marks. Each mark must be from 0 to 100.")
    else:
        total = 0
        for mark in marks:
            total = total + mark
        average = total / count
        if marks[-1] > marks[0]:
            trend = "Improved"
        elif marks[-1] < marks[0]:
            trend = "Declined"
        else:
            trend = "Unchanged"
        print("Assessment Marks:", marks)
        print("Average Mark:", round(average, 2))
        print("Performance Trend:", trend)