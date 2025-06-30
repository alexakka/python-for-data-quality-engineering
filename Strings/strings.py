text = """  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

words = text.lower().split()

words.extend([word[:-1] for word in words if "." in word])
normalized_words = []

for i, word in enumerate(words):
    if i == 0 or "." in words[i - 1]:
        normalized_words.append(word.capitalize())
    else:
        normalized_words.append(word)

for i, word in enumerate(normalized_words):
    if word.lower() == "iz":
        normalized_words[i] = normalized_words[i].replace("iz", "is")

normalized_text = " ".join(normalized_words)

print(normalized_text)

whitespaces = sum(1 for char in normalized_text if char.isspace())
print(f"The number of whitespaces in the text is {whitespaces}.")
