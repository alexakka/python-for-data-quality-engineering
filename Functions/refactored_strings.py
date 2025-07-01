def normalize_text(text: str):
    words = text.lower().split()

    words.extend([word[:-1] for word in words if "." in word])
    normalized_words = []

    for i, word in enumerate(words):
        if i == 0 or "." in words[i - 1]:
            normalized_words.append(word.capitalize())
        else:
            normalized_words.append(word)

    normalized_text = " ".join(normalized_words)

    return normalized_text


def correct_misspelling(text: str, old: str, new: str):
    words_list = text.split()
    for i, word in enumerate(words_list):
        if word.lower() == old.lower():
            words_list[i] = words_list[i].replace(old, new)

    corrected_text = " ".join(words_list)
    return corrected_text


def count_whitespaces(text: str):
    return sum(1 for char in text if char.isspace())




if __name__ == "__main__":
    text = """  tHis iz your homeWork, copy these Text to variable.



      You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



      it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE.



      last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
    """

    normalized_text = normalize_text(text)

    corrected_text = correct_misspelling(normalized_text, "iz", "is")
    print(corrected_text)

    whitespaces = count_whitespaces(corrected_text)
    print(f"The number of whitespaces in the text is {whitespaces}.")
