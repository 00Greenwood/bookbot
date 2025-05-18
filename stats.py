def get_num_words(text):
    words = text.split()
    return len(words)


def get_freq_chars(text):
    freq_chars = {}
    for char in text:
        char = char.lower()
        if char in freq_chars:
            freq_chars[char] += 1
        else:
            freq_chars[char] = 1
    return freq_chars


def get_sorted_chars(freq_chars):
    chars_list = []
    for char, num in freq_chars.items():
        chars_item = {}
        chars_item["char"] = char
        chars_item["num"] = num
        chars_list.append(chars_item)
    sorted_chars = sorted(chars_list, key=lambda x: x["num"], reverse=True)
    return sorted_chars
