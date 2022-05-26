# Write a python program that will replace a word with a given length by the provided word
# Example if I have a sentence:
# This is a brown fox
# Add more tests for this as an example below

sentence = "Beginners when start programming often get bored if they do not get a chance to " \
           "play with some interesting code."

sentence2 = "Beginners when start\n programming often get\t bored if they do not get a chance to " \
            "play with some interesting code."

sentence3 = "Beginners when start programming often get bored if they do not get a chance to " \
            "play with some interesting code."


def replace_words(text, length_to_replace, word):
    split_text = text.split()
    for i in range(0, len(split_text)):
        if len(split_text[i]) == length_to_replace:
            text = text.replace(split_text[i], word)
    return text


assert replace_words(sentence, 3,
                     "test") == "Beginners when start programming often test bored if they do test test a chance " \
                                "to play with some interesting code."

assert replace_words(sentence2, 3,
                     "test") == "Beginners when start\n programming often test\t bored if they do test test a chance " \
                                "to play with some interesting code."

assert replace_words(sentence3, 4,
                     "bear") == "Beginners bear start programming often get bored if bear do not get a chance to " \
                                "bear bear bear interesting code."
