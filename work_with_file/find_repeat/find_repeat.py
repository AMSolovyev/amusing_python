def get_file(in_file):
    input_file = open(in_file)
    line = input_file.read().replace('\n', '').lower().split()
    input_file.close()
    return line


def count_words_input_dict(line):
    count_word_in_text = dict()
    for word in line:
        if word not in count_word_in_text:
            count_word_in_text[word] = 1
        else:
            count_word_in_text[word] += 1
    return count_word_in_text


def find_max_repeat_words_in_text(count_word_in_text):
    max_value = max(count_word_in_text.values())
    for key, value in count_word_in_text.items():
        if value == max_value:
            final_dict = {key: value}
    return final_dict


def printer_result(final_dict):
    for key, value in final_dict.items():
        print(key, value)


if __name__ == '__main__':
    in_file = '/home/linux/Загрузки/dataset_3363_3.txt'
    
    loaded_file = get_file(in_file)
    counted_word = count_words_input_dict(loaded_file)
    find_repeats = find_max_repeat_words_in_text(counted_word)
    printer = printer_result(find_repeats)
   