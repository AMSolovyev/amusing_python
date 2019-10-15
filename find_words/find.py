text = input('Input text:  ').lower().split()

count_word_in_text = dict()
for word in text:
    if word not in count_word_in_text:
        count_word_in_text[word] = 1
    else:
        count_word_in_text[word] += 1
for keys, values in count_word_in_text.items():
    print(keys, values)
