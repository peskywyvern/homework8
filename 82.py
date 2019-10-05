# Write a function that takes a list of strings and removes those strings
# that don't consist of unique letters


def remove_string_doubles(strings: list) -> list:
    new_list = []
    for word in strings:
        counter = 0
        for character in word:
            counter += word.count(character)
        if counter == len(word):
            new_list.append(word)
    return new_list


assert remove_string_doubles(['cat', 'escape', 'template', 'head']) == \
       ['cat', 'head']
assert remove_string_doubles(['lamp', 'hash']) == ['lamp']


