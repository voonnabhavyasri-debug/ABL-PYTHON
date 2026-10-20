print("STRING-BASED EXAMINATION ANSWER EVALUATION")
model_answers = ["python", "cpu", "ram"]
correct = 0
for i in range(3):
    answer = input("Answer question " + str(i + 1) + ": ")
    answer = answer.strip().lower()
    if answer == model_answers[i]:
        correct = correct + 1
percentage = correct / 3 * 100
print("Correct Answers:", correct, "out of 3")
print("Total Marks:", correct)
print("Percentage:", round(percentage, 2), "%")