# 1. Fill the missing pieces of the count_even_numbers function
# Fill ____ pieces of the count_even_numbers implemention in order to pass the assertions.
# You can assume that numbers argument is a list of integers.

def count_even_numbers(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            count += 1
    return count


assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
assert count_even_numbers([1, 3, 5, 7]) == 0
assert count_even_numbers([-2, 2, -10, 8]) == 4


# 2. Searching for wanted people
# Implement find_wanted_people function which takes a list of names (strings) as argument.
# The function should return a list of names which are present both in WANTED_PEOPLE and in the name list given as
# argument to the function.

def find_wanted_people(names):
    return_list = []
    for wanted in WANTED_PEOPLE:
        for name in names:
            if wanted == name:
                return_list.append(name)
    return return_list


WANTED_PEOPLE = ['John Doe', 'Clint Eastwood', 'Chuck Norris']
people_to_check1 = ['Donald Duck', 'Clint Eastwood', 'John Doe', 'Barack Obama']
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert 'John Doe' in wanted1
assert 'Clint Eastwood' in wanted1

people_to_check2 = ['Donald Duck', 'Mickey Mouse', 'Zorro', 'Superman', 'Robin Hood']
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []


# 3. Counting average length of words in a sentence
# Create a function average_length_of_words which takes a string as an argument and returns the average
# length of the words in the string.
# You can assume that there is a single space between each word and that the input does not have punctuation.
# The result should be rounded to one decimal place (hint: see round).

def average_length_of_words(ave_string):
    words = ave_string.split()
    num_words = len(words)
    num_chars = 0
    for word in words:
        num_chars += len(word)

    return round(num_chars / num_words, 1) if (num_words > 0) else 0


assert average_length_of_words('only four erwo rdss') == 4
assert average_length_of_words('one two three') == 3.7
assert average_length_of_words('one two three four') == 3.8
assert average_length_of_words('') == 0
