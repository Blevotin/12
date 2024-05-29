def single_root_words(root_word, *other_words):
    same_words = []
    new_other_words = []
    root_word = root_word.lower()
    for word in other_words:
        new_other_words.append(word.lower())

    for i in new_other_words:
        if root_word in i:
            same_words.append(i)
    return same_words

print(single_root_words(input("введите корень: "),  "Коз", "козtr", "Козreg", "коgf", "dfgfdgз"))


