print("STUDENT FEEDBACK SENTIMENT SCORING")
feedback = input("Enter student feedback: ").lower()
words = feedback.replace(".", "").replace(",", "").split()
positive_words = ["good", "excellent", "helpful", "clear", "great", "useful"]
negative_words = ["bad", "poor", "confusing", "boring", "difficult", "late"]
positive_count = 0
negative_count = 0
for word in words:
    if word in positive_words:
        positive_count = positive_count + 1
    if word in negative_words:
        negative_count = negative_count + 1
score = positive_count - negative_count
print("Positive words:", positive_count)
print("Negative words:", negative_count)
print("Sentiment score:", score)
if score > 0:
    print("Sentiment: Positive")
elif score < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")