def disemvowel(string_):
    vowels = ['a', 'i', 'e', 'o', 'u']

    for letter in string_:
        if letter.lower() in vowels:
            string_ = string_.replace(letter, '')
    return string_


disemvowel("Hello")
