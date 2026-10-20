print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")
marks = []
for i in range(3):
    mark = int(input("Enter marks for subject " + str(i + 1) + " (0-100): "))
    marks.append(mark)

valid = True
for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if not valid:
    print("Invalid marks. Marks must be between 0 and 100.")
else:
    final_marks = marks.copy()
    grace_left = 5
    grace_used = 0

    for i in range(3):
        needed = 35 - final_marks[i]
        if needed > 0 and needed <= grace_left:
            final_marks[i] = final_marks[i] + needed
            grace_left = grace_left - needed
            grace_used = grace_used + needed

    print("\nOriginal marks:", marks)
    print("Final marks:", final_marks)
    print("Grace marks used:", grace_used)

    passed = True
    for mark in final_marks:
        if mark < 35:
            passed = False

    if passed:
        print("Final Result: PASS")
    else:
        print("Final Result: FAIL")