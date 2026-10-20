print("TEXT COMPRESSION USING CHARACTER RUNS")
text = input("Enter text: ")
compressed = ""
if len(text) > 0:
    current = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current:
            count = count + 1
        else:
            compressed = compressed + current + str(count)
            current = text[i]
            count = 1
    compressed = compressed + current + str(count)
print("Original text:", text)
print("Compressed text:", compressed)